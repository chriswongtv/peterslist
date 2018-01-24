<template>
  <div id="main">
    <a id="logo">
      <span>Peters</span>list
      <el-dropdown>
        <el-button class="navbar-button">
          <img src="../assets/img/housing.svg">
          <i class="el-icon-arrow-down el-icon--right"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>Housing</el-dropdown-item>
          <el-dropdown-item>Job</el-dropdown-item>
          <el-dropdown-item>Event</el-dropdown-item>
          <el-dropdown-item>Item Sale</el-dropdown-item>
          <el-dropdown-item>Lost + Found</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </a>
    <div id="search-panel" v-if="searchPanelType === ''" :class="{ clicked: searchPanelType !== '' }">
      <div id="search-panel-icons" v-if="searchPanelType === ''">
        <el-row :gutter="10">
          <el-col :xs="12" :sm="8" :md="4" :lg="4">
            <router-link to="/housing">
              <div class="search-panel-icon"
                  v-on:click="showSearchPanel('housing')"
                  :class="{ active: searchPanelType === 'housing' }">
                <!-- House by hans draiman from the Noun Project -->
                <img src="../assets/img/housing.svg">
              </div>
            </router-link>
            <span class="search-panel-label">HOUSING</span>
          </el-col>
          <el-col :xs="12" :sm="8" :md="4" :lg="4">
            <router-link to="/job">
              <div class="search-panel-icon"
                  v-on:click="showSearchPanel('job')"
                  :class="{ active: searchPanelType === 'job' }">
                <!-- Briefcase by mikicon from the Noun Project -->
                <img src="../assets/img/job.svg">
              </div>
            </router-link>
            <span class="search-panel-label">JOB</span>
          </el-col>
          <el-col :xs="12" :sm="8" :md="4" :lg="4">
            <router-link to="/event">
              <div class="search-panel-icon"
                  v-on:click="showSearchPanel('event')"
                  :class="{ active: searchPanelType === 'event' }">
                <!-- Ticket by Awesome from the Noun Project -->
                <img src="../assets/img/event.svg">
              </div>
            </router-link>
            <span class="search-panel-label">EVENT</span>
          </el-col>
          <el-col :xs="12" :sm="8" :md="4" :lg="4">
            <router-link to="/sale">
              <div class="search-panel-icon"
                  v-on:click="showSearchPanel('sale')"
                  :class="{ active: searchPanelType === 'sale' }">
                <!-- sales tag by Mihail Zhukov from the Noun Project -->
                <img src="../assets/img/sale.svg">
              </div>
            </router-link>
            <span class="search-panel-label">ITEM SALE</span>
          </el-col>
          <el-col :xs="12" :sm="8" :md="4" :lg="4">
            <router-link to="/lostandfound">
              <div class="search-panel-icon"
                  v-on:click="showSearchPanel('lostandfound')"
                  :class="{ active: searchPanelType === 'lostandfound' }">
                <!-- Heart by Lorena Salagre from the Noun Project -->
                <img src="../assets/img/romance.svg">
              </div>
            </router-link>
            <span class="search-panel-label">LOST+FOUND</span>
          </el-col>
          <el-col :xs="12" :sm="8" :md="4" :lg="4">
            <router-link to="/search">
              <div class="search-panel-icon"
                  v-on:click="showSearchPanel('search')"
                  :class="{ active: searchPanelType === 'search' }">
                <!-- Search by Deepz from the Noun Project -->
                <img src="../assets/img/search.svg">
              </div>
            </router-link>
            <span class="search-panel-label">SEARCH</span>
          </el-col>
        </el-row>
      </div>
    </div>
    <div id="search-type-container" v-if="searchPanelType !== ''">
      <router-view></router-view>
      <!-- <el-row :gutter="10">
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
              :format-tooltip="formatPriceRange">
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
          <div id="housing-results" class="result-container" v-if="searchPanelType === 'housing'">
            <el-row :gutter="30">
              <el-col :md="8" v-for="item in housingSearchResults" :key="item.postID">
                <el-card :body-style="{ padding: '0px' }">
                  <a :href="'/housing/' + item.postID">
                    <img :src="item.postInfo.photos" class="image">
                  </a>
                  <div class="card-details">
                    <a :href="'/housing/' + item.postID">{{ item.localityName }}</a>
                    <div class="bottom">
                    Available {{ formatDate(item.startDate) }} for ${{ item.postInfo.amount }}/month
                    </div>
                  </div>
                </el-card>
              </el-col> -->
              <!-- <el-col :md="8">
                <el-card :body-style="{ padding: '0px' }">
                  <img src="https://images.unsplash.com/photo-1486304873000-235643847519?dpr=2&auto=format&fit=crop&w=1500&h=844&q=80&cs=tinysrgb&crop=&bg=" class="image">
                  <div style="padding: 14px;">
                    <span>UTC Berkeley</span>
                    <div class="bottom">
                    Available June 16 for $650/month
                    </div>
                  </div>
                </el-card>
              </el-col>
              <el-col :md="8">
                <el-card :body-style="{ padding: '0px' }">
                  <img src="https://images.unsplash.com/photo-1488805990569-3c9e1d76d51c?dpr=2&auto=format&fit=crop&w=1500&h=1001&q=80&cs=tinysrgb&crop=&bg=" class="image">
                  <div style="padding: 14px;">
                    <span>VDC Norte Sublease</span>
                    <div class="bottom">
                    Available June 29 for $950/month
                    </div>
                  </div>
                </el-card>
              </el-col>
              <el-col :md="8">
                <el-card :body-style="{ padding: '0px' }">
                  <img src="https://images.unsplash.com/photo-1463620910506-d0458143143e?dpr=2&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=" class="image">
                  <div style="padding: 14px;">
                    <span>Oxford Court</span>
                    <div class="bottom">
                    Available July 1 for $720/month
                    </div>
                  </div>
                </el-card>
              </el-col> -->
            <!-- </el-row>
          </div>
        </el-col>
      </el-row>
      <div id="event-results" class="result-container" v-if="searchPanelType === 'event'">

      </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      searchPanelType: '', // Changes when a new 'type' is selected
      timeout: null, // For cancelTimeout() purposes
      urlQueries: {}, // For URL queries storage
      searchQuery: '',
      jobSearchOptions: {
        jobSearchTitleInput: '',
        jobSearchLocationInput: 'Irvine, CA',
        jobSearchCategories: ['All',
                              'Accounting',
                              'Admin & Clerical',
                              'Art & Design',
                              'Automotive',
                              'Banking',
                              'Biotech',
                              'Business & Management',
                              'Construction',
                              'Consultant',
                              'Customer Service',
                              'Education',
                              'Engineering',
                              'Film & Video',
                              'Finance',
                              'Food & Beverage',
                              'General Labor',
                              'Government',
                              'Hospitality',
                              'Human Resources',
                              'Information Technology',
                              'Legal',
                              'Manufacturing',
                              'Marketing & PR',
                              'Media & Journalism',
                              'Medical & Health',
                              'Nonprofit',
                              'Other',
                              'Real Estate',
                              'Retail',
                              'Sales',
                              'Science',
                              'Software & Technology',
                              'Transportation'],
        jobSearchCategory: 0
      },
      jobSearchResuts: '',
      eventSearchOptions: {
        eventSearchInput: '',
        eventSearchCategories: ['All',
                                'Arts & Music',
                                'Camps, Trips & Retreats',
                                'Career',
                                'Charity & Causes',
                                'Class, Training & Workshops',
                                'Concerts & Performance',
                                'Conferences & Seminars',
                                'Festivals & Fairs',
                                'Food & Drink',
                                'Games & Competitions',
                                'Hobbies & Special Interest',
                                'Networking',
                                'Other',
                                'Parties & Social Gatherings',
                                'Religion & Spirituality',
                                'Science & Technology',
                                'Sports & Fitness',
                                'Travel & Outdoor'],
        eventSearchCategory: 0,
        eventSearchDate: '0'
      },
      eventSearchResults: '',
      itemSaleSearchOptions: {
        itemSaleSearchCategories: [ 'All',
                                    'Bicycles',
                                    'Books',
                                    'Cars & Motorcycles',
                                    'Cell phones',
                                    'Clothing & Accessories',
                                    'Computers',
                                    'Electronics',
                                    'Furniture',
                                    'Health & Beauty',
                                    'Household Items',
                                    'Musical Instruments',
                                    'Other',
                                    'Photo/Video',
                                    'Skateboards & Scooters',
                                    'Sporting Goods',
                                    'Tickets',
                                    'Tools',
                                    'Toys & Games',
                                    'Video Games'],
        itemSaleSearchCategory: 0,
        itemSaleSearchInput: ''
      },
      itemSaleResults: '',
      lostAndFoundSearchOptions: {
        lostFoundSwitch: 'I lost',
        lostFoundSearchInput: ''
      },
      globalSearchInput: ''
    }
  },
  mounted: function() {
    this.searchPanelType = this.$router.currentRoute.path.substring(1)
  },
  watch: {

  },
  computed: {

  },
  methods: {
    showSearchPanel: function(type) {
      this.searchPanelType = type;
    },
    formatPriceRange: function(val) {
      if (val === 1500) {
        return '$1500+';
      } else {
        return '$' + val;
      }
    },
    formatDate: function(val) {
      var month = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
      ];

      var date = new Date(val);

      if (date <= new Date()) {
        return 'now';
      } else {
        return month[date.getMonth()] + ' ' + date.getDate();
      }
    },
    getQueryString: function() {
      var query = this.$router.currentRoute.query;
      var p = {}

      for (var q in query) {
        p[q] = query[q];
      }

      return p;
    },
    searchJob: function() {

    },
    searchEvent: function() {

    },
    searchItemSale: function() {

    },
    searchLostAndFound: function() {

    },
    searchAll: function() {

    }
  }
};
</script>

<style>
#main {
  background-image: url('../assets/img/bg.jpg');
  background-size: cover;
  background-position: center center;
  height: 100%;
  width: 100%;
  position: relative;
  overflow: scroll;
}

#main::before {
  content: '';
  background-image: linear-gradient(to bottom right, #0064a4 0%, #3d99be 40%, #ffd200 100%);
  opacity: 0.8;
  width: 100%;
  height: 100%;
  position: fixed;
}

#main #logo {
  position: absolute;
}

/* Search */
#search-panel {
  width: 50%;
  margin-left: auto;
  margin-right: auto;
  padding-top: 20%;
  transition: all .3s ease;
}

#search-panel.clicked {
  padding-top: 12vh;
}

#search-panel-icons {
  width: 100%;
  transition: all 5s ease;
}

.search-panel-icon {
  display: block;
  background: rgba(255,255,255,0.85);
  width: 100%;
  height: 0;
  padding-bottom: 100%;
  border-radius: 5px;
  transition: background .5s ease;
}

.search-panel-icon:hover {
  background: rgba(255,255,255,0.95);
  cursor: pointer;
}

.search-panel-icon.active {
  background: rgba(255,255,255,1);
}

.search-panel-icon>img {
  width: 50%;
  padding: 25%;
}

.search-panel-label {
  display: block;
  text-align: center;
  letter-spacing: 0.12em;
  font-size: 0.85em;
  margin-top: 5%;
  color: rgba(255,255,255,0.95);
}

#search-panel-options {
  width: 100%;
  background: rgba(255,255,255,0.85);
  border-radius: 5px;
  position: relative;
  margin-top: 2.5%;
  padding: 5% 0;
}

.search-type-container-enter-active, .search-type-container-leave-active {
  transition: all 0.5s ease;
}

.search-type-container-enter, .search-type-container-leave-to {
  transform: translateY(10px);
  opacity: 0;
}

#search-panel-options>div {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}

#search-panel-options .el-date-editor.el-input {
  width: 100%;
}

label {
  font-size: 12px;
  color: #48576a;
  line-height: 1.75;
  text-align: left;
  display: inline-block;
}

#search-panel-options label {
  margin-left: 2px;
}

.search-box {
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 2.5%;
  width: 60%;
}

/* Results Global */
#search-type-container {
  padding: 10% 5% 5% 5%;
}

.result-filter-container {
  position: relative;
  margin-left: auto;
  margin-right: auto;
  background-color: rgba(236, 240, 241,0.8);
  border-radius: 5px;
  padding: 5%;
}

.result-filter-container .el-select, .result-filter-container .el-input {
  width: 100%;
}

.result-container {
  position: relative;
  margin-left: auto;
  margin-right: auto;
  background-color: rgba(236, 240, 241,0.8);
  border-radius: 5px;
  padding: 2.5%;
}

/* Card */
.el-card img {
  max-height: 120px;
  min-width: 100%;
}

.el-card a {
  text-decoration: none;
  color: initial;
}

.el-card a:hover {
  cursor: pointer;
}

.bottom {
  font-size: 13px;
  color: #999;
}

.card-details {
  padding: 10px 14px 14px 14px;
}

/* Event */
#search-panel-event .el-dropdown, #search-panel-event button {
  width: 100%;
}
</style>