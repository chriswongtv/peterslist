<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
html, body {
  height: 100%;
}

body {
  margin: 0;
  font-family: 'Rubik', sans-serif;
}

.center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.center-left {
  display: flex;
  align-items: center;
}

.full-width {
  width: 100%;
}

#app {
  height: 100%;
}

/* Navbar Global */
#header {
  height: 80px;
  background: linear-gradient(to right, #0064a4 0%, #3d99be 40%, #ffd200 100%);
  padding: 0 2.5%;
}

#logo {
  top: 5%;
  left: 4%;
  color: rgba(255,255,255,0.95);
  font-weight: 300;
  font-size: 2em;
  letter-spacing: 0.005em;
  text-decoration: none;
}

#logo>span {
  font-weight: 500;
}

.navbar-button {
  border: none;
  margin-left: 15px;
  height: 100%;
  padding: 0;
}

.el-form--label-top .el-form-item__label {
  padding: 0;
}
</style>
