ELEMENT.locale(ELEMENT.lang.en)

var main = new Vue({
	el: '#main',
	data: {
		searchPanelType: '',
		housingSearchOptions: {
			housingDateStart: new Date(),
			housingOptions: ['Parking', 'Private bathroom', 'Pets allowed'],
			housingCheckbox: [],
			housingSearchRoommate: '0',
			housingPriceRange: [450, 1250]
		},
		housingSearchResults: '',
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
		eventSearchDate: '0',
		lostFoundSwitch: 'I lost',
		lostFoundSearchInput: ''
	},
	delimiters: ['[[',']]'],
	mounted: function() {

	},
	watch: {
		searchPanelType: function(val) {
			if (val === 'housing')
				this.searchHousing();
		},
		'housingSearchOptions.housingDateStart': function() {
			this.searchHousing();
		},
		'housingSearchOptions.housingCheckbox': function() {
			this.searchHousing();
		},
		'housingSearchOptions.housingSearchRoommate': function() {
			this.searchHousing();
		},
		'housingSearchOptions.housingPriceRange': function() {
			this.searchHousing();
		}
	},
	computed: {

	},
	methods: {
		showSearchPanel: function(type) {
			this.searchPanelType = type;
		},
		handleSearch: function() {
			alert(this.searchInput);
		},
		handleEventSearch: function() {

		},
		formatPriceRange: function(val) {
			if (val == 1500)
				return '$1500+';
			else
				return '$' + val;
		},
		formatDate: function(val) {
			var month = [
				"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
			];

			var date = new Date(val);

			if (date <= new Date())
				return 'now';
			else
				return month[date.getMonth()] + ' ' + date.getDate();
		},
		searchHousing: function() {
			var params = {}
			params.type = 'Housing'

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

			if (this.housingSearchOptions.housingPriceRange[1] < 1500)
				params.end_price = this.housingSearchOptions.housingPriceRange[1];

			params.movein_date = this.housingSearchOptions.housingDateStart;

			if (this.housingSearchOptions.housingCheckbox.indexOf("Parking") !== -1)
				params.parking = true;

			if (this.housingSearchOptions.housingCheckbox.indexOf("Private bathroom") !== -1)
				params.bathroom = true;

			if (this.housingSearchOptions.housingCheckbox.indexOf("Pets allowed") !== -1)
				params.pets = true;

			axios.get('/api/search', {
				params: params
			}).then(res => {
				this.housingSearchResults = res.data;
			})
		}
	}
});

var listing = new Vue({
	el: '#listing',
});