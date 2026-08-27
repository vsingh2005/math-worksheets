<?php
/**
 * Plugin Name: KSS Math Portal & Question Bank Manager
 * Plugin URI: https://kidsstemstudio.com/
 * Description: Integrates the Kids STEM Studio Math Placement Assessment Portal into WordPress. Features an Admin Panel Question Bank Editor, shortcodes for Elementor, and REST API endpoints.
 * Version: 2.0.0
 * Author: Kids STEM Studio
 * Author URI: https://kidsstemstudio.com/
 * License: GPLv2 or later
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class KSS_Math_Portal_Plugin {

    public function __construct() {
        // Activation hook to populate initial default questions
        register_activation_hook(__FILE__, array($this, 'plugin_activate'));

        // Admin menu
        add_action('admin_menu', array($this, 'register_admin_menu'));

        // REST API routes
        add_action('rest_api_init', array($this, 'register_rest_routes'));

        // Elementor / Theme Shortcodes
        add_shortcode('kss_math_login', array($this, 'render_login_shortcode'));
        add_shortcode('kss_math_portal', array($this, 'render_portal_shortcode'));
        add_shortcode('kss_math_instructions', array($this, 'render_instructions_shortcode'));
        add_shortcode('kss_math_exam', array($this, 'render_exam_shortcode'));
        add_shortcode('kss_math_results', array($this, 'render_results_shortcode'));

        // Enqueue Assets
        add_action('wp_enqueue_scripts', array($this, 'enqueue_frontend_assets'));
    }

    public function plugin_activate() {
        if (!get_option('kss_math_question_bank')) {
            $default_questions = $this->get_default_question_bank();
            update_option('kss_math_question_bank', json_encode($default_questions));
        }
    }

    public function enqueue_frontend_assets() {
        // Enqueue tailwind CDN and dashicons
        wp_enqueue_style('dashicons');
    }

    public function register_admin_menu() {
        add_menu_page(
            'KSS Math Portal',
            'Math Portal',
            'manage_options',
            'kss-math-portal',
            array($this, 'render_admin_page'),
            'dashicons-calculator',
            30
        );
    }

    public function render_admin_page() {
        if (!current_user_can('manage_options')) {
            return;
        }

        // Handle Form Submissions
        $message = '';
        if (isset($_POST['kss_save_question'])) {
            check_admin_referer('kss_question_action', 'kss_nonce');
            $this->handle_save_question($_POST);
            $message = 'Question saved successfully!';
        } elseif (isset($_POST['kss_delete_question'])) {
            check_admin_referer('kss_question_action', 'kss_nonce');
            $this->handle_delete_question(intval($_POST['question_id']));
            $message = 'Question deleted successfully!';
        } elseif (isset($_POST['kss_reset_default_bank'])) {
            check_admin_referer('kss_question_action', 'kss_nonce');
            update_option('kss_math_question_bank', json_encode($this->get_default_question_bank()));
            $message = 'Question Bank reset to default template!';
        }

        $raw_questions = get_option('kss_math_question_bank', '[]');
        $questions = json_decode($raw_questions, true) ?: array();

        $edit_question = null;
        if (isset($_GET['action']) && $_GET['action'] === 'edit' && isset($_GET['id'])) {
            $edit_id = intval($_GET['id']);
            foreach ($questions as $q) {
                if ($q['id'] === $edit_id) {
                    $edit_question = $q;
                    break;
                }
            }
        }
        ?>
        <div class="wrap">
            <h1 style="display:flex; align-items:center; gap:10px;">
                <span class="dashicons dashicons-calculator" style="font-size:32px; width:32px; height:32px;"></span>
                Kids STEM Studio Math Assessment — Question Bank Manager
            </h1>
            <p>Manage the adaptive math placement question bank served dynamically to students on your website.</p>

            <?php if (!empty($message)): ?>
                <div class="notice notice-success is-dismissible"><p><?php echo esc_html($message); ?></p></div>
            <?php endif; ?>

            <div style="display: flex; gap: 20px; margin-top: 20px; flex-wrap: wrap;">
                
                <!-- LEFT COLUMN: QUESTION BANK TABLE -->
                <div style="flex: 2; min-width: 600px; background: #fff; border: 1px solid #ccd0d4; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                    <div style="display:flex; justify-between; align-items:center; margin-bottom:15px;">
                        <h2 style="margin:0;">Current Question Bank (<?php echo count($questions); ?> Questions)</h2>
                        <form method="post" onsubmit="return confirm('Are you sure you want to reset the Question Bank to default?');">
                            <?php wp_nonce_field('kss_question_action', 'kss_nonce'); ?>
                            <input type="hidden" name="kss_reset_default_bank" value="1">
                            <button type="submit" class="button button-secondary">Reset to Default Bank</button>
                        </form>
                    </div>

                    <table class="wp-list-table widefat fixed striped">
                        <thead>
                            <tr>
                                <th style="width: 50px;">ID</th>
                                <th style="width: 60px;">Grade</th>
                                <th style="width: 150px;">Domain</th>
                                <th>Question Text</th>
                                <th style="width: 110px;">Type</th>
                                <th style="width: 120px;">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php if (empty($questions)): ?>
                                <tr><td colspan="6">No questions found. Click "Reset to Default Bank" to pre-fill standard questions.</td></tr>
                            <?php else: ?>
                                <?php foreach ($questions as $q): ?>
                                    <tr>
                                        <td><strong>#<?php echo esc_html($q['id']); ?></strong></td>
                                        <td><span class="badge" style="background:#e0f2fe; color:#0369a1; padding:3px 8px; border-radius:12px; font-weight:bold; font-size:11px;">Grade <?php echo esc_html($q['grade']); ?></span></td>
                                        <td><?php echo esc_html($q['domain']); ?></td>
                                        <td><?php echo esc_html(mb_strimwidth($q['text'], 0, 70, '...')); ?></td>
                                        <td><em><?php echo esc_html($q['type']); ?></em></td>
                                        <td>
                                            <a href="<?php echo admin_url('admin.php?page=kss-math-portal&action=edit&id=' . $q['id']); ?>" class="button button-small">Edit</a>
                                            <form method="post" style="display:inline-block;" onsubmit="return confirm('Delete this question?');">
                                                <?php wp_nonce_field('kss_question_action', 'kss_nonce'); ?>
                                                <input type="hidden" name="kss_delete_question" value="1">
                                                <input type="hidden" name="question_id" value="<?php echo esc_attr($q['id']); ?>">
                                                <button type="submit" class="button button-small button-link-delete">Delete</button>
                                            </form>
                                        </td>
                                    </tr>
                                <?php endforeach; ?>
                            <?php endif; ?>
                        </tbody>
                    </table>
                </div>

                <!-- RIGHT COLUMN: ADD / EDIT QUESTION FORM -->
                <div style="flex: 1; min-width: 320px; background: #fff; border: 1px solid #ccd0d4; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); align-self: flex-start;">
                    <h2><?php echo $edit_question ? 'Edit Question #' . esc_html($edit_question['id']) : 'Add New Question'; ?></h2>
                    <form method="post">
                        <?php wp_nonce_field('kss_question_action', 'kss_nonce'); ?>
                        <input type="hidden" name="kss_save_question" value="1">
                        <input type="hidden" name="question_id" value="<?php echo esc_attr($edit_question ? $edit_question['id'] : 0); ?>">

                        <p>
                            <label><strong>Grade Level:</strong></label><br>
                            <select name="grade" style="width:100%;" required>
                                <?php for ($g = 3; $g <= 8; $g++): ?>
                                    <option value="<?php echo $g; ?>" <?php selected($edit_question ? $edit_question['grade'] : 3, $g); ?>>Grade <?php echo $g; ?></option>
                                <?php endfor; ?>
                            </select>
                        </p>

                        <p>
                            <label><strong>Domain / Topic:</strong></label><br>
                            <input type="text" name="domain" style="width:100%;" value="<?php echo esc_attr($edit_question ? $edit_question['domain'] : ''); ?>" required placeholder="e.g. Fractions, Ratios, Algebra">
                        </p>

                        <p>
                            <label><strong>Question Type:</strong></label><br>
                            <select name="type" id="kss_qtype" style="width:100%;" onchange="toggleQuestionTypeFields()">
                                <option value="multiple-choice" <?php selected($edit_question ? $edit_question['type'] : 'multiple-choice', 'multiple-choice'); ?>>Multiple Choice</option>
                                <option value="numeric-response" <?php selected($edit_question ? $edit_question['type'] : '', 'numeric-response'); ?>>Numeric Response</option>
                            </select>
                        </p>

                        <p>
                            <label><strong>Question Text:</strong></label><br>
                            <textarea name="text" style="width:100%; height:80px;" required><?php echo esc_textarea($edit_question ? $edit_question['text'] : ''); ?></textarea>
                        </p>

                        <!-- MULTIPLE CHOICE OPTIONS -->
                        <div id="mc_options_field">
                            <label><strong>Options (Check the correct answer):</strong></label>
                            <?php 
                            $opts = ($edit_question && isset($edit_question['options'])) ? $edit_question['options'] : array(
                                array('text' => '', 'correct' => true),
                                array('text' => '', 'correct' => false),
                                array('text' => '', 'correct' => false),
                                array('text' => '', 'correct' => false),
                            );
                            for ($i = 0; $i < 4; $i++):
                                $val = isset($opts[$i]['text']) ? $opts[$i]['text'] : '';
                                $is_c = isset($opts[$i]['correct']) && $opts[$i]['correct'];
                            ?>
                                <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                                    <input type="radio" name="correct_mc_index" value="<?php echo $i; ?>" <?php checked($is_c); ?>>
                                    <input type="text" name="options[<?php echo $i; ?>]" value="<?php echo esc_attr($val); ?>" style="flex:1;" placeholder="Option <?php echo ($i+1); ?>">
                                </div>
                            <?php endfor; ?>
                        </div>

                        <!-- NUMERIC RESPONSE -->
                        <div id="numeric_option_field" style="display:none;">
                            <p>
                                <label><strong>Numeric Correct Answer:</strong></label><br>
                                <input type="text" name="correct_numeric_answer" style="width:100%;" value="<?php echo esc_attr($edit_question ? (isset($edit_question['correctAnswer']) ? $edit_question['correctAnswer'] : '') : ''); ?>" placeholder="e.g. 24 or 3.5">
                            </p>
                        </div>

                        <p>
                            <label><strong>Step-by-Step Explanation:</strong></label><br>
                            <textarea name="explanation" style="width:100%; height:70px;" required placeholder="Detailed solution explanation for students..."><?php echo esc_textarea($edit_question ? $edit_question['explanation'] : ''); ?></textarea>
                        </p>

                        <p style="margin-top:15px;">
                            <button type="submit" class="button button-primary button-large" style="width:100%;">Save Question</button>
                            <?php if ($edit_question): ?>
                                <a href="<?php echo admin_url('admin.php?page=kss-math-portal'); ?>" class="button button-secondary" style="width:100%; margin-top:6px; text-align:center;">Cancel Edit</a>
                            <?php endif; ?>
                        </p>
                    </form>
                </div>

            </div>
        </div>

        <script>
            function toggleQuestionTypeFields() {
                var qtype = document.getElementById('kss_qtype').value;
                if (qtype === 'numeric-response') {
                    document.getElementById('mc_options_field').style.display = 'none';
                    document.getElementById('numeric_option_field').style.display = 'block';
                } else {
                    document.getElementById('mc_options_field').style.display = 'block';
                    document.getElementById('numeric_option_field').style.display = 'none';
                }
            }
            toggleQuestionTypeFields();
        </script>
        <?php
    }

    private function handle_save_question($data) {
        $raw = get_option('kss_math_question_bank', '[]');
        $questions = json_decode($raw, true) ?: array();

        $id = intval($data['question_id']);
        $grade = intval($data['grade']);
        $domain = sanitize_text_field($data['domain']);
        $text = sanitize_textarea_field($data['text']);
        $type = sanitize_text_field($data['type']);
        $explanation = sanitize_textarea_field($data['explanation']);

        $question_obj = array(
            'id' => ($id > 0) ? $id : (count($questions) > 0 ? max(array_column($questions, 'id')) + 1 : 101),
            'grade' => $grade,
            'domain' => $domain,
            'text' => $text,
            'type' => $type,
            'explanation' => $explanation
        );

        if ($type === 'multiple-choice') {
            $opts = array();
            $correct_idx = isset($data['correct_mc_index']) ? intval($data['correct_mc_index']) : 0;
            if (isset($data['options']) && is_array($data['options'])) {
                foreach ($data['options'] as $idx => $opt_text) {
                    $opts[] = array(
                        'text' => sanitize_text_field($opt_text),
                        'correct' => ($idx === $correct_idx)
                    );
                }
            }
            $question_obj['options'] = $opts;
        } else {
            $question_obj['correctAnswer'] = sanitize_text_field($data['correct_numeric_answer']);
        }

        if ($id > 0) {
            foreach ($questions as $index => $q) {
                if ($q['id'] === $id) {
                    $questions[$index] = $question_obj;
                    break;
                }
            }
        } else {
            $questions[] = $question_obj;
        }

        update_option('kss_math_question_bank', json_encode($questions));
    }

    private function handle_delete_question($id) {
        $raw = get_option('kss_math_question_bank', '[]');
        $questions = json_decode($raw, true) ?: array();
        $filtered = array_values(array_filter($questions, function($q) use ($id) {
            return $q['id'] !== $id;
        }));
        update_option('kss_math_question_bank', json_encode($filtered));
    }

    public function register_rest_routes() {
        register_rest_route('kss-math/v1', '/questions', array(
            'methods' => 'GET',
            'callback' => array($this, 'rest_get_questions'),
            'permission_callback' => '__return_true'
        ));

        register_rest_route('kss-math/v1', '/save-attempt', array(
            'methods' => 'POST',
            'callback' => array($this, 'rest_save_attempt'),
            'permission_callback' => '__return_true'
        ));
    }

    public function rest_get_questions() {
        $raw = get_option('kss_math_question_bank', '[]');
        $questions = json_decode($raw, true) ?: array();
        return rest_ensure_response($questions);
    }

    public function rest_save_attempt($request) {
        $params = $request->get_json_params();
        if (empty($params)) {
            return new WP_Error('invalid_data', 'No data provided', array('status' => 400));
        }

        $attempts = get_option('kss_math_saved_attempts', array());
        $attempts[] = $params;
        update_option('kss_math_saved_attempts', $attempts);

        return rest_ensure_response(array('success' => true, 'message' => 'Attempt saved successfully'));
    }

    // SHORTCODE RENDERS FOR ELEMENTOR
    public function render_login_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/login.html" style="width:100%; height:800px; border:none; border-radius:16px;"></iframe></div>';
    }

    public function render_portal_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/portal.html" style="width:100%; height:900px; border:none; border-radius:16px;"></iframe></div>';
    }

    public function render_instructions_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/instructions.html" style="width:100%; height:750px; border:none; border-radius:16px;"></iframe></div>';
    }

    public function render_exam_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/exam.html" style="width:100%; height:950px; border:none; border-radius:16px;"></iframe></div>';
    }

    public function render_results_shortcode() {
        return '<div class="kss-embed-wrapper"><iframe src="' . plugin_dir_url(__FILE__) . 'assets/results.html" style="width:100%; height:1100px; border:none; border-radius:16px;"></iframe></div>';
    }

    private function get_default_question_bank() {
        return array(
            array(
                "id" => 101, "grade" => 3, "domain" => "Multiplication Concepts",
                "text" => "A bakery boxes donuts in groups of 6. If a customer buys 4 boxes, how many donuts do they get in total?",
                "type" => "multiple-choice",
                "options" => array(
                    array("text" => "24", "correct" => true),
                    array("text" => "10", "correct" => false),
                    array("text" => "18", "correct" => false),
                    array("text" => "12", "correct" => false)
                ),
                "explanation" => "Multiply the number of boxes by the number of donuts per box: 4 x 6 = 24."
            ),
            array(
                "id" => 102, "grade" => 3, "domain" => "Multiplication Properties",
                "text" => "Which equation shows the Commutative Property of Multiplication?",
                "type" => "multiple-choice",
                "options" => array(
                    array("text" => "4 x 5 = 5 x 4", "correct" => true),
                    array("text" => "4 x 5 = 20", "correct" => false),
                    array("text" => "(4 x 2) x 5 = 4 x (2 x 5)", "correct" => false),
                    array("text" => "4 x 0 = 0", "correct" => false)
                ),
                "explanation" => "The Commutative Property states that changing the order of factors does not change the product: a x b = b x a."
            ),
            array(
                "id" => 103, "grade" => 3, "domain" => "Division Concepts",
                "text" => "If 32 books are shared equally among 4 shelves, how many books go on each shelf?",
                "type" => "numeric-response",
                "correctAnswer" => "8",
                "explanation" => "Divide the total books by the number of shelves: 32 / 4 = 8 books per shelf."
            )
        );
    }
}

new KSS_Math_Portal_Plugin();
