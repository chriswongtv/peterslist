ELEMENT.locale(ELEMENT.lang.en)

// Router instance and paths
const router = new VueRouter({
	routes: [
		{ path: '/housing' },
		{ path: '/job' },
		{ path: '/event' },
		{ path: '/sale' },
		{ path: '/lostandfound' },
		{ path: '/search' }
	]
})

// Main module
var main = new Vue({
	router,
	el: '#main',
	data: {
		searchPanelType: '', // Changes when a new "type" is selected
		timeout: null, // For cancelTimeout() purposes
		urlQueries: {}, // For URL queries storage
		housingSearchOptions: {
			housingDateStart: new Date(), // Sets the move-in date to today by default
			housingOptions: ['Parking', 'Private bathroom', 'Pets allowed'], // The options to be displayed in the checkbox
			housingCheckbox: [], // Contains the options selected from housingOptions
			housingSearchRoommate: '0', // The number of desired roommates
			housingPriceRange: [450, 1250] // Default price range
		},
		housingSearchResults: '', // Stores all the search results
		jobSearchOptions: {
			jobSearchTitleInput: '',
			jobSearchLocationInput: 'Irvine, CA',
			jobSearchCategories: [	'All',
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
			eventSearchDate: '0',
		},
		eventSearchResults: '',
		itemSaleSearchOptions: {
			itemSaleSearchCategories: [	'All',
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
			clearTimeout(this.timeout);

			this.timeout = setTimeout(() => {
				var query = this.getQueryString();

				query.sp = this.housingSearchOptions.housingPriceRange[0];
				query.ep = this.housingSearchOptions.housingPriceRange[1];

				router.replace({ query: query })

				this.searchHousing();
			}, 500)
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
			// Restore options from URL query
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
				this.housingSearchResults = res.data; // Store the results
			})
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
}).$mount('#main')

router.beforeEach((to, from, next) => {
	// Save "from" queries
	main.urlQueries[from.path.substring(1)] = from.query;
	// If "to" doesn't have queries, check for existence and load if necessary
	if (Object.keys(to.query).length === 0 && to.query.constructor === Object && main.urlQueries[to.path.substring(1)]) {
		to.query = main.urlQueries[to.path.substring(1)];
	}
	next();
})