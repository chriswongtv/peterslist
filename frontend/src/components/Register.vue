<template>
  <div id="register">
    <div id="header" class="center-left">
      <a href="/" id="logo">
        <span>Peters</span>list
      </a>
    </div>
    <div class="form-container">
      <el-form ref="form" label-position="top" :model="form" label-width="120px">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="First Name">
              <el-input v-model="form.firstName" placeholder="Peter"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Last Name">
              <el-input v-model="form.lastName" placeholder="Anteater"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item label="Email">
          <el-input v-model="form.email" placeholder="panteater@uci.edu"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <el-input v-model="form.password" type="password"></el-input>
        </el-form-item>
        <el-form-item label="Phone Number">
          <el-input v-model="form.phone" placeholder="949-123-4567"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="register">Register</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Register',
  data () {
    return {
      form: {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        phone: ''
      }
    }
  },
  mounted: function() {
    if (this.isLoggedIn()) {
      this.$router.push('/');
    }
  },
  watch: {

  },
  methods: {
    register: function() {
      axios.post('http://cacofonix-1.ics.uci.edu:5000/api/signup', this.form)
        .then((response) => {
          console.log(response);
          if (response.status === 200) {
            this.$notify({
              title: 'Success',
              message: 'Your account has been created.',
              type: 'success'
            });

            this.setUser(this.form.email);
            this.$router.push('/');
          } else {
            this.$notify.error({
              title: 'Registration Failed',
              message: 'Please try again later.'
            });
          }
        })
    }
  }
}
</script>

<style scoped>
.form-container {
  width: 80%;
  margin-top: 3%;
  margin-left: auto;
  margin-right: auto;
}

.el-select {
  width: 100%;
}

button {
  width: 100%;
}
</style>