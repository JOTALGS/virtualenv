import { useUserStore } from '@/stores/user';
import axios from 'axios';

export default (await import('vue')).defineComponent({
setup() {
const userStore = useUserStore();

return {
userStore
};
},

data() {
return {
searchQuery: '',
display: false, // Inicialmente oculto
collabs: [],
searchTerm: '',
suggestions: [],
trends: [],
showSuggestions: false,
showTrends: false,
inputValue: '',
};
},

components: {
Toast
},

beforeCreate() {
this.userStore.initStore();

const token = this.userStore.user.access;

if (token) {
axios.defaults.headers.common["Authorization"] = "Bearer " + token;
} else {
axios.defaults.headers.common["Authorization"] = "";
}
},

methods: {
search() {
// Aquí puedes manejar la lógica de búsqueda
console.log('Buscando:', this.searchQuery);
},
toggleDisplay() {
this.display = !this.display; // Cambiar estado de visibilidad
},
closePopUp(event) {
const popup = document.querySelector('#popup');
const navbar = document.querySelector('#navbar');

if (!popup.contains(event.target) && !navbar.contains(event.target)) {
this.display = false;
}
},
getTrends() {
},

async getUserSuggestions(event) {
if (this.searchTerm.length === 0) {
this.showSuggestions = false;
return;
}

this.inputValue = event.target.value;

async; axios
.get(`/api/search/users/${this.inputValue}/`)
.then(response => {

this.suggestions = response.data.suggestions;
this.showSuggestions = true;
})
.catch(error => {
console.log('error search:', error);
});

axios
.get(`/api/posts/trends/${this.inputValue}/`)
.then(response => {
this.trends = response.data.trends_found;
console.log('trends', response.data.trends_found);

// Select the top two trends
this.trends = this.trends.slice(0, 2);

})
.catch(error => {
console.log('Error: ', error);
});
},

selectSuggestion(suggestion) {
this.searchTerm = suggestion.name;
this.showSuggestions = false;
// Perform search or other action based on selected suggestion
},
},

mounted() {
// Add event listener to close pop-up when clicking outside of it
document.body.addEventListener('click', this.closePopUp);
this.getTrends();
this.getUserSuggestions();
},
beforeUnmount() {
// Remove event listener when component is unmounted
document.body.removeEventListener('click', this.closePopUp);
},
});
