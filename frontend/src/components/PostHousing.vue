<template>
  <div id="post-housing">
    <div id="header" class="center-left">
      <a href="/" id="logo">
        <span>Peters</span>list
      </a>
    </div>
    <el-menu default-active="0" class="post-housing-tab-bar" mode="horizontal" @select="handleTabSelect">
      <el-menu-item index="0">Lease</el-menu-item>
      <el-menu-item index="1">For Sale</el-menu-item>
    </el-menu>
    <div class="form-container">
      <el-form ref="form" :model="form" label-width="120px" v-if="!index">
        <el-form-item label="Locality Name">
          <el-input v-model="form.localityName" placeholder="Mesa Court"></el-input>
        </el-form-item>
        <el-form-item label="Address">
          <el-input v-model="form.buildingNumber" placeholder="Building Number"></el-input>
          <el-input v-model="form.streetName" placeholder="Street Name"></el-input>
          <el-input v-model="form.city" placeholder="City"></el-input>
          <el-input v-model="form.state" placeholder="State"></el-input>
          <el-input v-model="form.zip" placeholder="Zip"></el-input>
        </el-form-item>
        <el-form-item label="Price">
          <el-input class="price" v-model="form.price" placeholder="$550"></el-input> / month
        </el-form-item>
        <el-form-item label="Home Type">
          <el-select v-model="form.homeType" placeholder="Please select your home type">
            <el-option label="House" value="House"></el-option>
            <el-option label="Apartment" value="Apartment"></el-option>
            <el-option label="Townhouse" value="Townhouse"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Date Available">
          <el-col :span="11">
            <el-date-picker type="date" placeholder="Pick a date" v-model="form.dateAvailable" style="width: 100%;"></el-date-picker>
          </el-col>
          <el-col class="line" :span="2">-</el-col>
          <el-col :span="11">
            <el-date-picker type="date" placeholder="Pick a date" v-model="form.endDate" style="width: 100%;"></el-date-picker>
          </el-col>
        </el-form-item>
        <el-form-item label="Number of">
          <el-col :span="8">
            <el-input v-model="form.roommates" placeholder="Roommates"></el-input>
          </el-col>
          <el-col :span="8">
            <el-input v-model="form.occupants" placeholder="Occupants"></el-input>
          </el-col>
          <el-col :span="8">
            <el-input v-model="form.bedrooms" placeholder="Bedrooms"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="Amenities">
          <el-checkbox-group v-model="form.amenities">
            <el-checkbox label="Parking" name="type"></el-checkbox>
            <el-checkbox label="Private Bathroom" name="type"></el-checkbox>
            <el-checkbox label="Pets Allowed" name="type"></el-checkbox>
            <el-checkbox label="Furnished" name="type"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form-item label="Description">
          <el-input type="textarea" v-model="form.description"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">Post</el-button>
        </el-form-item>
      </el-form>
      
      <el-form ref="form" :model="form" label-width="120px" v-if="index">
        <el-form-item label="Locality Name">
          <el-input v-model="form.localityName" placeholder="Mesa Court"></el-input>
        </el-form-item>
        <el-form-item label="Address">
          <el-input v-model="form.buildingNumber" placeholder="Building Number"></el-input>
          <el-input v-model="form.streetName" placeholder="Street Name"></el-input>
          <el-input v-model="form.city" placeholder="City"></el-input>
          <el-input v-model="form.state" placeholder="State"></el-input>
          <el-input v-model="form.zip" placeholder="Zip"></el-input>
        </el-form-item>
        <el-form-item label="Price">
          <el-input class="price" v-model="form.price" placeholder="$550,000"></el-input>
        </el-form-item>
        <el-form-item label="Home Type">
          <el-select v-model="form.homeType" placeholder="Please select your home type">
            <el-option label="House" value="House"></el-option>
            <el-option label="Apartment" value="Apartment"></el-option>
            <el-option label="Townhouse" value="Townhouse"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Date Available">
          <el-date-picker type="date" placeholder="Pick a date" v-model="form.dateAvailable" style="width: 100%;"></el-date-picker>
        </el-form-item>
        <el-form-item label="Number of">
          <el-col :span="12">
            <el-input v-model="form.bedrooms" placeholder="Bedrooms"></el-input>
          </el-col>
          <el-col :span="12">
            <el-input v-model="form.bathrooms" placeholder="Bathrooms"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="Amenities">
          <el-checkbox-group v-model="form.amenities">
            <el-checkbox label="Pool" name="type"></el-checkbox>
            <el-checkbox label="Gym" name="type"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form-item label="Description">
          <el-input type="textarea" v-model="form.description"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="postHousing">Post</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PostHousing',
  data () {
    return {
      index: 0,
      form: {
        localityName: '',
        buildingNumber: '',
        streetName: '',
        state: '',
        city: '',
        zip: '',
        price: '',
        homeType: '',
        dateAvailable: '',
        endDate: '',
        roommates: '',
        occupants: '',
        bedrooms: '',
        bathrooms: '',
        amenities: [],
        description: ''
      }
    }
  },
  mounted: function() {

  },
  watch: {

  },
  methods: {
    handleTabSelect: function(key) {
      this.index = parseInt(key);
    },
    postHousing: function() {

    }
  }
}
</script>

<style scoped>
.post-housing-tab-bar>li {
  width: 50%;
  text-align: center;
}

.form-container {
  width: 80%;
  margin-top: 5%;
  margin-left: auto;
  margin-right: auto;
}

.el-select {
  width: 100%;
}

.price {
  width: 100px;
  margin-right: 5px;
}

.line {
  text-align: center;
}

button {
  width: 100%;
}
</style>