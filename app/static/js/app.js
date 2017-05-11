ELEMENT.locale(ELEMENT.lang.en)

var main = new Vue({
	el: '#main',
	data: {
		searchPanelType: '',
		searchInput: '',
		searchDateRangeStart: null,
		searchDateRangeEnd: null
	},
	mounted: function() {

	},
	watch: {

	},
	methods: {
		showSearchPanel: function(type) {
			this.searchPanelType = type;
		},
		handleSearch: function() {
			alert(this.searchInput);
		}
	}
});