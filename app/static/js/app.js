ELEMENT.locale(ELEMENT.lang.en)

var main = new Vue({
	el: '#main',
	data: {
		searchPanelType: '',
		housingDateStart: new Date(),
		housingOptions: ['Parking', 'Private bathroom', 'Pets allowed'],
		housingCheckbox: [],
		housingRoommate: '0',
		housingPriceRange: [450, 1250],
		eventSearchInput: '',
		eventSearchDate: '0'
	},
	delimiters: ['[[',']]'],
	mounted: function() {

	},
	watch: {

	},
	computed: {
		housingSearchRoommateLabel: function() {
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
			}
		},
		eventSearchDateLabel: function() {
			switch (this.eventSearchDate) {
				case '0':
					return 'All Dates';
				case '1':
					return 'Today';
				case '2':
					return 'Tomorrow';
				case '3':
					return 'This Week';
				case '4':
					return 'This Weekend';
				case '5':
					return 'Next Week';
				case '6':
					return 'Next Month';
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
		setHousingSearchRoommate: function(option) {
			this.housingRoommate = option;
		},
		setEventSearchDate: function(option) {
			this.eventSearchDate = option;
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