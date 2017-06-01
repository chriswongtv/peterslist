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
			housingPriceRange: [450, 1250],
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
		housingSearchOptions: function() {
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

			// switch (this.housingSearchRoommate) {
			// 	case '1':
			// 		params.
			// }



			axios.get('/api/search', {
				params: params
			}).then(res => {
				this.housingSearchResults = res.data.results;
			})
		}
	}
});