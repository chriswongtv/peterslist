<template>
  <transition name="search-type-container">
    <div>
      <div class="search-box">
        <el-input placeholder="Search" v-model="housingSearchOptions.housingSearchQuery" class="input-with-select">
          <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>
      </div>
      <el-row :gutter="10">
        <el-col :md="5">
          <div class="result-filter-container">
            <label>Room Type</label>
            <el-select v-model="housingSearchOptions.housingSearchRoommate" placeholder="All Rooms">
              <el-option label="All Rooms" value="0">
              </el-option>
              <el-option label="Single Room" value="1">
              </el-option>
              <el-option label="Double Room" value="2">
              </el-option>
              <el-option label="Triple Room" value="3">
              </el-option>
              <el-option label="4+ Room" value="4">
              </el-option>
            </el-select>

            <label>Price Range</label>
            <el-slider
              v-model="housingSearchOptions.housingPriceRange"
              range
              :min="200"
              :max="1500"
              :format-tooltip="$parent.formatPriceRange">
            </el-slider>  

            <label>Move-In Date</label>
            <el-date-picker
              v-model="housingSearchOptions.housingDateStart"
              type="date"
              placeholder="Move-in Date">
            </el-date-picker>

            <label>Additional Filters</label>
            <el-checkbox-group v-model="housingSearchOptions.housingCheckbox">
              <el-checkbox-button v-for="option in housingSearchOptions.housingOptions" :label="option" :key="option">{{option}}</el-checkbox-button>
            </el-checkbox-group>
          </div>
        </el-col>
        <el-col :md="19">
          <div id="housing-results" class="result-container">
            <el-row :gutter="30">
              <el-col :md="8" v-for="item in housingSearchResults" :key="item.postID">
                <el-card :body-style="{ padding: '0px' }">
                  <a :href="'/housing/' + item.postID">
                    <img :src="item.postInfo.photos" class="image">
                  </a>
                  <div class="card-details">
                    <a :href="'/housing/' + item.postID">{{ item.localityName }}</a>
                    <div class="bottom">
                    Available {{ $parent.formatDate(item.startDate) }} for ${{ item.postInfo.amount }}/month
                    </div>
                  </div>
                </el-card>
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>
    </div>
  </transition>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HousingSearch',
  data () {
    return {
      timeout: null,
      housingSearchOptions: {
        housingSearchQuery: '',
        housingDateStart: new Date(), // Sets the move-in date to today by default
        housingOptions: ['Parking', 'Private bathroom', 'Pets allowed'], // The options to be displayed in the checkbox
        housingCheckbox: [], // Contains the options selected from housingOptions
        housingSearchRoommate: '0', // The number of desired roommates
        housingPriceRange: [450, 1250] // Default price range
      },
      housingSearchResults: '' // Stores all the search results
    }
  },
  mounted: function() {
    this.loadHousingOptions();
  },
  watch: {
    'housingSearchOptions.housingSearchQuery': function() {
      clearTimeout(this.timeout);

      var query = this.$parent.getQueryString();
      query.q = encodeURI(this.housingSearchOptions.housingSearchQuery);
      this.$router.replace({ query: query })

      this.timeout = setTimeout(() => {
        this.searchHousing();
      }, 500)
    },
    'housingSearchOptions.housingDateStart': function() {
      var query = this.$parent.getQueryString();

      query.date = this.housingSearchOptions.housingDateStart.toLocaleDateString();

      this.$router.replace({ query: query })

      this.searchHousing();
    },
    'housingSearchOptions.housingCheckbox': function() {
      var query = this.$parent.getQueryString();

      if (this.housingSearchOptions.housingCheckbox.indexOf('Parking') !== -1) {
        query.parking = 1;
      } else {
        delete query.parking;
      }

      if (this.housingSearchOptions.housingCheckbox.indexOf('Private bathroom') !== -1) {
        query.bath = 1;
      } else {
        delete query.bath;
      }

      if (this.housingSearchOptions.housingCheckbox.indexOf('Pets allowed') !== -1) {
        query.pets = 1;
      } else {
        delete query.pets;
      }

      this.$router.replace({ query: query })

      this.searchHousing();
    },
    'housingSearchOptions.housingSearchRoommate': function() {
      var query = this.$parent.getQueryString();

      query.rm = this.housingSearchOptions.housingSearchRoommate;

      this.$router.replace({ query: query })

      this.searchHousing();
    },
    'housingSearchOptions.housingPriceRange': function() {
      clearTimeout(this.timeout);

      this.timeout = setTimeout(() => {
        var query = this.$parent.getQueryString();

        query.sp = this.housingSearchOptions.housingPriceRange[0];
        query.ep = this.housingSearchOptions.housingPriceRange[1];

        this.$router.replace({ query: query })

        this.searchHousing();
      }, 500)
    }
  },
  methods: {
    loadHousingOptions: function() {
      // Restore options from URL query
      for (var q in this.$router.currentRoute.query) {
        if (q === 'date') {
          this.housingSearchOptions.housingDateStart = new Date(this.$router.currentRoute.query[q]);
        } else if (q === 'rm') {
          this.housingSearchOptions.housingSearchRoommate = this.$router.currentRoute.query[q];
        } else if (q === 'sp') {
          this.housingSearchOptions.housingPriceRange[0] = this.$router.currentRoute.query[q];
        } else if (q === 'ep') {
          this.housingSearchOptions.housingPriceRange[1] = this.$router.currentRoute.query[q];
        } else if (q === 'parking') {
          this.housingSearchOptions.housingCheckbox.push('Parking');
        } else if (q === 'bath') {
          this.housingSearchOptions.housingCheckbox.push('Private bathroom');
        } else if (q === 'pets') {
          this.housingSearchOptions.housingCheckbox.push('Pets allowed');
        } else if (q === 'q') {
          this.housingSearchOptions.housingSearchQuery = decodeURI(this.$router.currentRoute.query[q]);
        }
      };
    },
    searchHousing: function() {
      const vm = this;
      var params = {};
      params.type = 'Housing';

      if (this.housingSearchOptions.housingSearchQuery) {
        params.query = this.housingSearchOptions.housingSearchQuery;
      }

      // Adds parameters into the object
      switch (this.housingSearchOptions.housingSearchRoommate) {
        case '1':
          params.roommates = 0;
          break;
        case '2':
          params.roommates = 1;
          break;
        case '3':
          params.roommates = 2;
          break;
        case '4':
          params.roommates = 3;
          break;
        default:
      }

      params.start_price = this.housingSearchOptions.housingPriceRange[0];

      if (this.housingSearchOptions.housingPriceRange[1] < 1500) {
        params.end_price = this.housingSearchOptions.housingPriceRange[1];
      }

      params.movein_date = this.housingSearchOptions.housingDateStart;

      if (this.housingSearchOptions.housingCheckbox.indexOf('Parking') !== -1) {
        params.parking = true;
      }

      if (this.housingSearchOptions.housingCheckbox.indexOf('Private bathroom') !== -1) {
        params.bathroom = true;
      }

      if (this.housingSearchOptions.housingCheckbox.indexOf('Pets allowed') !== -1) {
        params.pets = true;
      }

      axios.get('http://localhost:5000/api/search', {
        params: params
      }).then(res => {
        vm.housingSearchResults = res.data; // Store the results
      });
    }
  }
}
</script>

<style scoped>
#search-panel-house {
  text-align: center;
}

#search-panel-house label {
  margin-left: 0;
}

#search-panel-house .el-col+.el-col+.el-col+.el-col {
  margin-top: 10px;
}

#search-panel-house .el-dropdown, #search-panel-house .el-dropdown>button {
  width: 100%;
}

#search-panel-house #housing-price {
  padding: 0 20px !important;
}

#housing-results .el-col+.el-col+.el-col+.el-col {
  padding-top: 30px;
}
</style>