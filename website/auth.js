/* =========================================================
   KIDS STEM STUDIO - AUTHENTICATION & SESSION MANAGER
   Shared module across all portal pages
   ========================================================= */

class AuthenticationManager {
  constructor() {
    this.users = JSON.parse(localStorage.getItem('kss_users')) || [];
    this.currentUser = null;
    this.allAttempts = JSON.parse(localStorage.getItem('kss_attempts')) || [];
    this.initDemoUsers();
    this.loadCustomSettings();
  }

  async loadCustomSettings() {
    try {
      const res = await fetch('/wp-json/kss-math/v1/settings');
      if (res.ok) {
        const s = await res.json();
        if (s.primary_color) document.documentElement.style.setProperty('--color-primary', s.primary_color);
        if (s.secondary_color) document.documentElement.style.setProperty('--color-secondary', s.secondary_color);
        if (s.brand_teal_color) document.documentElement.style.setProperty('--color-brand', s.brand_teal_color);
        if (s.navy_dark_color) document.documentElement.style.setProperty('--color-dark', s.navy_dark_color);
      }
    } catch (e) {
      // Use standard default CSS variables
    }
  }

  async hashPassword(password, salt) {
    const encoder = new TextEncoder();
    const data = encoder.encode(password + salt);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  }

  async initDemoUsers() {
    const salt1 = 'kss_salt_demo_1';
    const hash1 = await this.hashPassword('password123', salt1);
    const salt2 = 'kss_salt_demo_2';
    const hash2 = await this.hashPassword('stemstudio2026', salt2);

    const demoUser = {
      username: 'student1',
      email: 'student1@kidsstemstudio.com',
      passwordHash: hash1,
      salt: salt1,
      createdAt: new Date().toISOString(),
      attempts: []
    };

    const parentUser = {
      username: 'parent_demo',
      email: 'parent@kidsstemstudio.com',
      passwordHash: hash2,
      salt: salt2,
      createdAt: new Date().toISOString(),
      attempts: []
    };

    let needsSave = false;
    if (!this.users.some(u => u.username.toLowerCase() === 'student1')) {
      this.users.push(demoUser);
      needsSave = true;
    }
    if (!this.users.some(u => u.username.toLowerCase() === 'parent_demo')) {
      this.users.push(parentUser);
      needsSave = true;
    }

    if (needsSave) {
      this.saveUsersToStorage();
    }

    const storedAttempts = localStorage.getItem('kss_attempts');
    if (storedAttempts) {
      this.allAttempts = JSON.parse(storedAttempts);
    }

    const session = localStorage.getItem('kss_session') || sessionStorage.getItem('kss_session');
    if (session) {
      const found = this.users.find(u => u.username.toLowerCase() === session.toLowerCase());
      if (found) {
        this.currentUser = found;
        this.currentUser.token = localStorage.getItem('kss_jwt_token') || sessionStorage.getItem('kss_jwt_token');
        if (this.currentUser.token) {
          this.syncAttemptsFromServer();
        }
      }
    }

    this.updateHeaderUI();
  }

  saveUsersToStorage() {
    localStorage.setItem('kss_users', JSON.stringify(this.users));
  }

  saveAttemptsToStorage() {
    localStorage.setItem('kss_attempts', JSON.stringify(this.allAttempts));
  }

  requireAuth() {
    if (!this.currentUser) {
      const session = localStorage.getItem('kss_session') || sessionStorage.getItem('kss_session');
      if (!session) {
        window.location.href = 'login.html';
        return false;
      }
      const found = this.users.find(u => u.username.toLowerCase() === session.toLowerCase());
      if (found) {
        this.currentUser = found;
        this.updateHeaderUI();
        return true;
      }
      window.location.href = 'login.html';
      return false;
    }
    return true;
  }

  async registerUser(username, email, password) {
    username = username.trim();
    email = email.trim();
    if (!username || !email || !password) {
      throw new Error('Please fill in all registration fields.');
    }

    const existing = this.users.find(u => u.username.toLowerCase() === username.toLowerCase() || u.email.toLowerCase() === email.toLowerCase());
    if (existing) {
      throw new Error('Username or email address already registered.');
    }

    const salt = 'kss_salt_' + Math.random().toString(36).substring(2);
    const passwordHash = await this.hashPassword(password, salt);

    const newUser = {
      username: username,
      email: email,
      passwordHash: passwordHash,
      salt: salt,
      createdAt: new Date().toISOString(),
      attempts: []
    };

    this.users.push(newUser);
    this.saveUsersToStorage();
    this.currentUser = newUser;
    localStorage.setItem('kss_session', newUser.username);
    this.updateHeaderUI();
    return newUser;
  }

  async loginUser(usernameOrEmail, password, rememberMe) {
    usernameOrEmail = usernameOrEmail.trim();
    if (!usernameOrEmail || !password) {
      throw new Error('Username/Email and Password are required.');
    }

    let wpError = null;
    try {
      const response = await fetch('/wp-json/jwt-auth/v1/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: usernameOrEmail,
          password: password
        })
      });

      const contentType = response.headers.get('content-type') || '';
      if (contentType.includes('application/json')) {
        const data = await response.json();
        if (response.ok && data.token) {
          let user = this.users.find(u => u.username.toLowerCase() === data.user_nicename.toLowerCase());
          if (!user) {
            user = {
              username: data.user_nicename,
              email: data.user_email,
              createdAt: new Date().toISOString(),
              attempts: []
            };
            this.users.push(user);
            this.saveUsersToStorage();
          }

          this.currentUser = user;
          if (rememberMe) {
            localStorage.setItem('kss_session', user.username);
            localStorage.setItem('kss_jwt_token', data.token);
          } else {
            sessionStorage.setItem('kss_session', user.username);
            sessionStorage.setItem('kss_jwt_token', data.token);
          }

          console.log('WordPress JWT authentication successful for:', user.username);
          this.syncAttemptsFromServer();
          this.updateHeaderUI();
          return user;
        } else {
          wpError = data.message || 'WordPress authentication failed.';
        }
      } else {
        wpError = 'WordPress REST API is not responding with JSON.';
      }
    } catch (err) {
      wpError = err.message || 'WordPress connection failed.';
    }

    // Fallback local authentication
    const fallbackUser = this.users.find(u =>
      u.username.toLowerCase() === usernameOrEmail.toLowerCase() ||
      u.email.toLowerCase() === usernameOrEmail.toLowerCase()
    );

    if (fallbackUser && fallbackUser.salt) {
      const computedHash = await this.hashPassword(password, fallbackUser.salt);
      if (computedHash === fallbackUser.passwordHash) {
        this.currentUser = fallbackUser;
        if (rememberMe) {
          localStorage.setItem('kss_session', fallbackUser.username);
        } else {
          sessionStorage.setItem('kss_session', fallbackUser.username);
        }
        this.updateHeaderUI();
        return fallbackUser;
      }
    }

    if (wpError && !wpError.includes('connection failed') && !wpError.includes('Failed to fetch') && !wpError.includes('not responding with JSON')) {
      throw new Error(wpError);
    }
    throw new Error('Invalid username or password.');
  }

  logoutUser() {
    this.currentUser = null;
    localStorage.removeItem('kss_session');
    sessionStorage.removeItem('kss_session');
    localStorage.removeItem('kss_jwt_token');
    sessionStorage.removeItem('kss_jwt_token');
    window.location.href = 'login.html';
  }

  saveExamAttempt(attemptData) {
    const username = this.currentUser ? this.currentUser.username : 'Guest Student';
    const attempt = {
      id: 'att_' + Date.now(),
      username: username,
      timestamp: new Date().toISOString(),
      score: attemptData.score,
      totalQuestions: 15,
      timeElapsedSeconds: attemptData.timeElapsed,
      recommendedLevel: attemptData.recommendedLevel,
      answers: attemptData.answers
    };

    this.allAttempts.push(attempt);
    this.saveAttemptsToStorage();

    if (this.currentUser) {
      const userObj = this.users.find(u => u.username === this.currentUser.username);
      if (userObj) {
        if (!userObj.attempts) userObj.attempts = [];
        userObj.attempts.push(attempt.id);
        this.saveUsersToStorage();
      }

      const token = this.currentUser.token || localStorage.getItem('kss_jwt_token') || sessionStorage.getItem('kss_jwt_token');
      if (token) {
        fetch('/wp-json/kss-math/v1/save-attempt', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
          },
          body: JSON.stringify(attempt)
        }).catch(err => {
          console.error('Error syncing attempt to WordPress:', err);
        });
      }
    }
    return attempt;
  }

  getUserAttempts(username) {
    return this.allAttempts.filter(a => a.username.toLowerCase() === username.toLowerCase());
  }

  async syncAttemptsFromServer() {
    const token = this.currentUser ? (this.currentUser.token || localStorage.getItem('kss_jwt_token') || sessionStorage.getItem('kss_jwt_token')) : null;
    if (!token) return;

    try {
      const response = await fetch('/wp-json/kss-math/v1/get-attempts', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + token
        }
      });
      if (response.ok) {
        const data = await response.json();
        if (data.success && Array.isArray(data.attempts)) {
          const serverAttempts = data.attempts.map((att, index) => {
            return {
              id: 'att_server_' + index + '_' + Date.now(),
              username: this.currentUser.username,
              timestamp: att.timestamp,
              score: att.score,
              totalQuestions: 15,
              timeElapsedSeconds: att.timeElapsedSeconds,
              recommendedLevel: att.recommendedLevel,
              answers: att.answers || []
            };
          });

          const otherUsersAttempts = this.allAttempts.filter(a => a.username.toLowerCase() !== this.currentUser.username.toLowerCase());
          this.allAttempts = [...otherUsersAttempts, ...serverAttempts];
          this.saveAttemptsToStorage();
        }
      }
    } catch (err) {
      console.error('Error syncing attempts from server:', err);
    }
  }

  updateHeaderUI() {
    const headerWidget = document.getElementById('user-header-widget');
    if (!headerWidget) return;

    if (this.currentUser) {
      headerWidget.innerHTML = `
        <div class="flex items-center space-x-3 bg-slate-100 px-3.5 py-1.5 rounded-full border border-slate-200">
          <span class="w-7 h-7 rounded-full bg-kss-teal text-white flex items-center justify-center font-bold text-xs">
            ${this.currentUser.username.substring(0, 1).toUpperCase()}
          </span>
          <span class="text-xs font-extrabold text-navy-dark">${this.currentUser.username}</span>
          <button onclick="AuthManager.renderHistoryModal()" class="text-xs font-bold text-sky-600 hover:underline">📜 History</button>
          <button onclick="AuthManager.logoutUser()" class="text-xs font-bold text-rose-500 hover:underline">Logout</button>
        </div>
      `;
    } else {
      headerWidget.innerHTML = `
        <a href="login.html" class="px-4 py-2 text-xs font-bold text-white bg-sky-500 hover:bg-sky-600 rounded-lg transition-colors">Log In</a>
      `;
    }
  }

  renderHistoryModal() {
    const historyModal = document.getElementById('history-modal');
    const container = document.getElementById('user-history-content');
    if (!historyModal || !container) return;

    if (!this.currentUser) {
      container.innerHTML = `
        <div class="text-center py-8 text-slate-500 font-semibold">
          Please log in to view your saved math placement exam history.
        </div>
      `;
    } else {
      const attempts = this.getUserAttempts(this.currentUser.username);
      if (attempts.length === 0) {
        container.innerHTML = `
          <div class="text-center py-8 space-y-2">
            <span class="text-3xl">📋</span>
            <p class="text-slate-600 font-bold text-sm">No exam attempts found yet.</p>
            <p class="text-slate-400 text-xs">Complete a math assessment to view your solution breakdown here!</p>
          </div>
        `;
      } else {
        attempts.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
        let html = '';
        attempts.forEach(att => {
          const dateStr = new Date(att.timestamp).toLocaleString();
          const mins = Math.floor((att.timeElapsedSeconds || 0) / 60);
          const secs = (att.timeElapsedSeconds || 0) % 60;

          html += `
            <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-2 text-xs">
              <div class="flex justify-between items-center font-bold">
                <span class="text-navy-dark text-sm">${att.recommendedLevel}</span>
                <span class="text-emerald-600 bg-emerald-100 px-2.5 py-0.5 rounded-full">Score: ${att.score}/${att.totalQuestions}</span>
              </div>
              <div class="flex justify-between text-slate-500 font-medium">
                <span>Completed: ${dateStr}</span>
                <span>Time: ${mins}m ${secs}s</span>
              </div>
            </div>
          `;
        });
        container.innerHTML = html;
      }
    }

    if (window.openModal) {
      window.openModal('history-modal');
    } else if (historyModal) {
      historyModal.classList.remove('hidden');
      historyModal.classList.add('flex');
    }
  }
}

const AuthManager = new AuthenticationManager();
window.AuthManager = AuthManager;
