import Vue from 'vue'

Vue.mixin({
  data() {
    return {
      email: ''
    }
  },
  methods: {
    setUser: function(email) {
      this.email = email;
      window.localStorage.setItem('email', email);
    },
    getUser: function() {
      if (this.email === '') {
        this.email = window.localStorage.getItem('email');
      }

      return this.email;
    },
    isLoggedIn: function() {
      if (this.email === '' && !window.localStorage.getItem('email')) {
        return false;
      } else {
        return true;
      }
    },
    logout: function() {
      this.email = '';
      window.localStorage.removeItem('email');
    }
  }
})
