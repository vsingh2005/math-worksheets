# Kids STEM Studio Math Placement Portal
## HostGator & WordPress Update Guide (Modular Multi-Page Architecture)

This document provides step-by-step instructions for deploying and updating the **Modular Multi-Page Math Assessment Portal** on your HostGator hosting account and WordPress site.

---

## 1. Overview of the New Modular Structure

The codebase has been refactored into **isolated, dedicated modules for every page**. Each HTML page now loads only its own specific JavaScript logic, while sharing core authentication and styling.

### File Inventory (`website/` Directory)

| File | Purpose | Loaded By |
| :--- | :--- | :--- |
| **`login.html`** | Login UI, authentication forms, password reset dialog | Shortcode `[kss_math_login]` |
| **`login.js`** | Form handling, tab switching, password visibility, redirect | `login.html` |
| **`portal.html`** | Track selection dashboard, past attempts history modal | Shortcode `[kss_math_portal]` |
| **`portal.js`** | Track switcher, session state initializer, modal triggers | `portal.html` |
| **`instructions.html`** | Assessment guidelines, test rules, preparation checklist | Shortcode `[kss_math_instructions]` |
| **`instructions.js`** | Track validation, auth guard, modal triggers | `instructions.html` |
| **`exam.html`** | Adaptive test engine UI, progress sidebar, timer, question card | Shortcode `[kss_math_exam]` |
| **`exam.js`** | Adaptive difficulty engine, question presenter, timer, answer recorder | `exam.html` |
| **`questions.js`** | Default question bank (Grades 3–8) separated from the engine | `exam.html` |
| **`results.html`** | Score report UI, recommended placement badge, solution reviews | Shortcode `[kss_math_results]` |
| **`results.js`** | Score calculation, filterable solution breakdown, celebration confetti | `results.html` |
| **`auth.js`** | Shared session manager, SHA-256 hashing, WordPress REST API sync | All pages |
| **`index.css`** | Shared typography, color scheme tokens, and custom styles | All pages |
| **`index.html`** | Auto-router (redirects logged-in users to portal, others to login) | Root entry point |
| **Images** | `hero_kids_math_classroom_...png`, `success_celebration_...png`, `kss.png` | Various pages |

> **Key Benefit:** A bug or update in `exam.js` physically cannot break `login.html` or `portal.html`. Files are lightweight and cache independently on HostGator.

---

## 2. Step-by-Step HostGator Deployment Instructions

### Method A: Quick cPanel Upload (Recommended)

1. **Log in to HostGator cPanel:**
   * Go to `https://yourdomain.com:2083` (or your HostGator customer portal).
   * Open **File Manager**.

2. **Navigate to the Plugin Assets Directory:**
   * In File Manager, navigate to:
     ```text
     public_html/wp-content/plugins/kss-math-portal/assets/
     ```
   * *(If the folder does not exist, navigate to `public_html/wp-content/plugins/kss-math-portal/` and click **+ Folder** to create `assets`)*.

3. **Upload the Files:**
   * Click **Upload** in the top cPanel toolbar.
   * Upload all files from your local `website/` folder into `public_html/wp-content/plugins/kss-math-portal/assets/`:
     * `login.html` & `login.js`
     * `portal.html` & `portal.js`
     * `instructions.html` & `instructions.js`
     * `exam.html` & `exam.js`
     * `results.html` & `results.js`
     * `questions.js`
     * `auth.js`
     * `index.css`
     * `index.html`
     * Image assets (`.png`)

   > **Tip:** You can select all files inside `website/`, create a `.zip` archive on your computer, upload the `.zip` file via cPanel, right-click it in File Manager, and choose **Extract**.

4. **Verify WordPress Plugin Script (`kss-math-portal.php`):**
   * Ensure `wordpress/kss-math-portal.php` is located at:
     ```text
     public_html/wp-content/plugins/kss-math-portal/kss-math-portal.php
     ```

---

## 3. WordPress & Elementor Integration

Because the HTML filenames (`login.html`, `portal.html`, `exam.html`, `results.html`, `instructions.html`) remain unchanged, **your existing Elementor pages and shortcodes will continue to work immediately with zero re-linking required**.

### Available Shortcodes

| Shortcode | Target Page |
| :--- | :--- |
| `[kss_math_login]` | Embeds `assets/login.html` |
| `[kss_math_portal]` | Embeds `assets/portal.html` |
| `[kss_math_instructions]` | Embeds `assets/instructions.html` |
| `[kss_math_exam]` | Embeds `assets/exam.html` |
| `[kss_math_results]` | Embeds `assets/results.html` |

### Direct Testing URLs
You can test each page directly in your browser before checking inside Elementor:
* `https://yourdomain.com/wp-content/plugins/kss-math-portal/assets/login.html`
* `https://yourdomain.com/wp-content/plugins/kss-math-portal/assets/portal.html`
* `https://yourdomain.com/wp-content/plugins/kss-math-portal/assets/instructions.html`
* `https://yourdomain.com/wp-content/plugins/kss-math-portal/assets/exam.html`
* `https://yourdomain.com/wp-content/plugins/kss-math-portal/assets/results.html`

---

## 4. How to Update Individual Files in the Future

With this modular structure, you never have to re-upload the entire project when making small edits:

* **To change the login flow or styling:** Edit and upload only `login.html` or `login.js`.
* **To update exam logic or scoring rules:** Edit and upload only `exam.js`.
* **To add default math questions:** Edit and upload only `questions.js`.
* **To change the results layout or explanations:** Edit and upload only `results.html` or `results.js`.
* **To update color themes:** Edit your colors in **WordPress Admin Dashboard → Math Portal 🧮** (the plugin automatically syncs colors to the frontend via `/wp-json/kss-math/v1/settings`).

---

## 5. Troubleshooting & Cache Busting

1. **Browser Caching Old Scripts:**
   * If an updated script doesn't seem to take effect immediately, clear your browser cache or perform a hard refresh (`Ctrl + F5` on Windows, `Cmd + Shift + R` on Mac).
   * If using a WordPress caching plugin (e.g. WP Rocket, LiteSpeed Cache, W3 Total Cache) or Cloudflare, click **Purge Cache**.
2. **REST API Endpoints:**
   * The portal communicates with your WordPress database via:
     * `https://yourdomain.com/wp-json/kss-math/v1/settings`
     * `https://yourdomain.com/wp-json/kss-math/v1/questions`
     * `https://yourdomain.com/wp-json/kss-math/v1/save-attempt`
   * Ensure WordPress Permalinks are set to **Post name** (under **Settings → Permalinks**) so REST API routes resolve properly.
