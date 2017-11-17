<template>
  <div id="housing">
    <div id="header" class="center-left">
      <a href="/" id="logo">
        <span>Peters</span>list
      </a>
      <el-dropdown>
        <el-button class="navbar-button">
          <img src="../assets/img/housing.svg">
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>Action 1</el-dropdown-item>
          <el-dropdown-item>Action 2</el-dropdown-item>
          <el-dropdown-item>Action 3</el-dropdown-item>
          <el-dropdown-item>Action 4</el-dropdown-item>
          <el-dropdown-item>Action 5</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
    <div id="listing">
      <div class="photos">
        <div class="cover-image" :style="{ backgroundImage: 'url(' + listingInfo.postInfo.photos + ')' }"></div>
      </div>

      <div class="listing-details">
        <el-row :gutter="10">
          <el-col :md="16">
            <div class="listing-title">
              {{ listingInfo.localityName }}
            </div>
            <div class="listing-location">
              {{ listingInfo.postInfo.location.city }}, {{ listingInfo.postInfo.location.state }}
            </div>
            <div class="listing-description">
              {{ listingInfo.postInfo.description }}
            </div>
          </el-col>
          <el-col :md="8">
            <div class="container">
              Features
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HousingResult',
  data() {
    return {
      listingInfo: {
        localityName: '',
        postInfo: {
          photos: '',
          description: '',
          location: {
            city: '',
            state: ''
          }
        }
      }
    }
  },
  mounted: function() {
    const vm = this;

    axios.get('http://localhost:5000/api/getListing', {
      params: {
        id: this.$route.params.id
      }
    }).then(res => {
      vm.listingInfo = res.data[0]['p'];
      console.log(vm.listingInfo)
    });
  }
}
</script>

<style scoped>
#listing {
  height: 100%;
}

#listing .photos {
  height: 350px;
}

#listing .cover-image {
  height: 100%;
  width: 100%;
  background-size: cover;
  background-position: center center;
}

.listing-details {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 2.5%;
}

.listing-title {
  font-size: 2.5em;
  font-weight: 700;
}

.listing-location {
  font-size: 1.2em;
  padding-top: 2.5px;
  padding-bottom: 10px;
  font-weight: 300;
}

.listing-description {
  padding-top: 1%;
}

.container {
  /*position: relative;
  width: 80%;
  margin-left: auto;
  margin-right: auto;*/
  background-color: rgba(236, 240, 241,0.8);
  border-radius: 5px;
  padding: 2.5%;
  top: 17%;
}
</style>