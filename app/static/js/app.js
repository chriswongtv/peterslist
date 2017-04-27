var main = new Vue({
	el: '#main',
	data: {
		searchPanelType: ''
	},
	mounted: function() {

	},
	watch: {

	},
	methods: {
		showSearchPanel: function(type) {
			this.searchPanelType = type;
		}
	}
});