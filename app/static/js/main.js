ELEMENT.locale(ELEMENT.lang.en)

const housingSearchPanel = {
	template: ''
}

const router = new VueRouter({
	routes: [{ path: '/housing', name: 'housing', component: housingSearchPanel }]
})

var main = new Vue({
	router,
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
		this.searchPanelType = router.currentRoute.path.substring(1)

		if (this.searchPanelType === 'housing')
			this.loadHousingOptions();
	},
	watch: {
		searchPanelType: function(val) {
			if (val === 'housing')
				this.searchHousing();
		},
		'housingSearchOptions.housingDateStart': function() {
			var query = this.getQueryString();

			query.date = this.housingSearchOptions.housingDateStart.toLocaleDateString();

			router.replace({ query: query })

			this.searchHousing();
		},
		'housingSearchOptions.housingCheckbox': function() {
			var query = this.getQueryString();

			if (this.housingSearchOptions.housingCheckbox.indexOf('Parking') !== -1)
				query.parking = 1;
			else
				delete query.parking;

			if (this.housingSearchOptions.housingCheckbox.indexOf('Private bathroom') !== -1)
				query.bath = 1;
			else
				delete query.bath;

			if (this.housingSearchOptions.housingCheckbox.indexOf('Pets allowed') !== -1)
				query.pets = 1;
			else
				delete query.pets;

			router.replace({ query: query })

			this.searchHousing();
		},
		'housingSearchOptions.housingSearchRoommate': function() {
			var query = this.getQueryString();

			query.rm = this.housingSearchOptions.housingSearchRoommate;

			router.replace({ query: query })

			this.searchHousing();
		},
		'housingSearchOptions.housingPriceRange': function() {
			var query = this.getQueryString();

			query.sp = this.housingSearchOptions.housingPriceRange[0];
			query.ep = this.housingSearchOptions.housingPriceRange[1];

			router.replace({ query: query })

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
		getQueryString: function() {
			var query = router.currentRoute.query;
			var p = {}

			for (q in query) {
				p[q] = query[q];
			}

			return p;
		},
		loadHousingOptions: function() {
			for (q in router.currentRoute.query) {
				if (q === 'date')
					this.housingSearchOptions.housingDateStart = new Date(router.currentRoute.query[q]);
				else if (q === 'rm')
					this.housingSearchOptions.housingSearchRoommate = router.currentRoute.query[q];
				else if (q === 'sp')
					this.housingSearchOptions.housingPriceRange[0] = router.currentRoute.query[q];
				else if (q === 'ep')
					this.housingSearchOptions.housingPriceRange[1] = router.currentRoute.query[q];
				else if (q === 'parking')
					this.housingSearchOptions.housingCheckbox.push('Parking');
				else if (q === 'bath')
					this.housingSearchOptions.housingCheckbox.push('Private bathroom');
				else if (q === 'pets')
					this.housingSearchOptions.housingCheckbox.push('Pets allowed');
			}
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
}).$mount('#main')