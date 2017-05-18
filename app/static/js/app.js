ELEMENT.locale(ELEMENT.lang.en)

var main = new Vue({
	el: '#main',
	data: {
		searchPanelType: '',
		searchInput: '',
		searchDateRangeStart: null,
		searchDateRangeEnd: null,
		housingOptions: ['Parking', 'Private bathroom', 'Pets allowed'],
		housingCheckbox: [],
		housingRoommate: '',
		housingPriceRange: ''
	},
	delimiters: ['[[',']]'],
	mounted: function() {

	},
	watch: {

	},
	computed: {
		housingRoommateLabel: function() {
			switch (this.housingRoommate) {
				case '0':
					return 'All';
				case '1':
					return '1 (Single)';
				case '2':
					return '2 (Double)';
				case '3':
					return '3 (Triple)';
				case '4':
					return '4+';
				default:
					return 'Room Type';
			}
		}
	},
	methods: {
		showSearchPanel: function(type) {
			this.searchPanelType = type;
		},
		handleSearch: function() {
			alert(this.searchInput);
		},
		setHousingRoommate: function(option) {
			this.housingRoommate = option;
		},
		formatPriceRange: function(val) {
			if (val == 1500)
				return '$1500+';
			else
				return '$' + val;
		}
	}
});