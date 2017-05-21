ELEMENT.locale(ELEMENT.lang.en)

var main = new Vue({
	el: '#main',
	data: {
		searchPanelType: '',
		housingDateStart: new Date(),
		housingOptions: ['Parking', 'Private bathroom', 'Pets allowed'],
		housingCheckbox: [],
		housingSearchRoommate: '0',
		housingPriceRange: [450, 1250],
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
	delimiters: ['[[',']]'],
	mounted: function() {

	},
	watch: {

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
		}
	}
});