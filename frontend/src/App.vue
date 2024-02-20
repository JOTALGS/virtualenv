<template>
    <div class="relative">
      <nav id="navbar" class="py-4 px-8 bg-teal-500 border-b border-gray-200">
        <div class="max-w-7xl mx-auto">
            <div class="flex items-center justify-between">
                <div class="menu-left">
                    <a href="#" class="font-mono text-4xl">TRIBU</a>
                </div>
                <div v-if="userStore.user.isAuthenticated">
                  <div class="">
                    <div class="inline-flex flex-col justify-center relative text-gray-500">
                        <div @click="toggleDisplay" class="relative">
                            <input type="text" v-model="searchTerm" @input="handleInput" class="p-2 pl-8 rounded border border-gray-200 bg-gray-200 focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-600 focus:border-transparent" placeholder="search..." />
                            <svg class="w-4 h-4 absolute left-2.5 top-3.5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                            </svg>
                        </div>
                    </div>
                </div>
                </div>

                <div class="menu-center flex">
                </div>

                <div class="menu-right flex items-center space-x-4">
                  <template v-if="userStore.user.isAuthenticated">
                    <RouterLink :to="{'name': 'feed'}" class="">
                      <a href="#Feed" class="text-black-100">
                        <div class="px-6 py-3 border border-gray-500 rounded bg-cyan-700 hover:bg-blue-300 flex items-center space-x-2">
                          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
                            <path d="M23 9v2h-2v7a3 3 0 01-3 3h-4v-6h-4v6H6a3 3 0 01-3-3v-7H1V9l11-7 5 3.18V2h3v5.09z"></path>
                          </svg>
                        </div>
                      </a>
                    </RouterLink>

                    <RouterLink :to="{'name': 'profile', params: {'id': userStore.user.id}}" class="">
                      <a href="#" class="text-black-100">
                        <div class="px-6 py-3 border border-gray-500 rounded bg-cyan-700 hover:bg-blue-300 flex items-center space-x-2">
                          <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 9.776c.112-.017.227-.026.344-.026h15.812c.117 0 .232.009.344.026m-16.5 0a2.25 2.25 0 0 0-1.883 2.542l.857 6a2.25 2.25 0 0 0 2.227 1.932H19.05a2.25 2.25 0 0 0 2.227-1.932l.857-6a2.25 2.25 0 0 0-1.883-2.542m-16.5 0V6A2.25 2.25 0 0 1 6 3.75h3.879a1.5 1.5 0 0 1 1.06.44l2.122 2.12a1.5 1.5 0 0 0 1.06.44H18A2.25 2.25 0 0 1 20.25 9v.776" />
                          </svg>
                        </div>
                      </a>
                    </RouterLink>

                    <RouterLink :to="{'name': 'about'}" class="">
                      <a href="#" class="text-black-100">
                        <div class="px-6 py-3 border border-gray-500 rounded bg-cyan-700 hover:bg-blue-300 flex items-center space-x-2">
                          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                            <path fill-rule="evenodd" d="M5.25 9a6.75 6.75 0 0 1 13.5 0v.75c0 2.123.8 4.057 2.118 5.52a.75.75 0 0 1-.297 1.206c-1.544.57-3.16.99-4.831 1.243a3.75 3.75 0 1 1-7.48 0 24.585 24.585 0 0 1-4.831-1.244.75.75 0 0 1-.298-1.205A8.217 8.217 0 0 0 5.25 9.75V9Zm4.502 8.9a2.25 2.25 0 1 0 4.496 0 25.057 25.057 0 0 1-4.496 0Z" clip-rule="evenodd" />
                          </svg>
                        </div>             
                      </a>
                    </RouterLink>
                  </template>

                  <template v-else>
                    <RouterLink to="/login" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Log in</RouterLink>
                    <RouterLink to="/signup" class="py-4 px-6 bg-blue-600 text-white rounded-lg">Sign up</RouterLink>
                  </template>
                </div>
            </div>
        </div>
    </nav>

    <div v-show="display" id="popup" class="absolute inset-16 bg-gray-900 bg-opacity-50">
      <div>
        <ul class="bg-white border border-blue-300 w-full mt-2 rounded-lg">
          <li>Results:</li>
          <div v-if="showTrends"
              v-for="trend in trends"
              v-bind:key="trend.id"
              @click="selectTrend(trend)"
              >
            <RouterLink :to="{name: 'trendview', params: {id: trend.hashtag}}" class="" onclick="window.location.reload()">
              <li class="pl-8 pr-2 py-1 border-b-2 border-gray-100 rounded-lg relative cursor-pointer hover:bg-yellow-50 hover:text-gray-900">
                  
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="stroke-current absolute w-4 h-4 left-2 top-2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 0 0 2.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 0 0-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75 2.25 2.25 0 0 0-.1-.664m-5.8 0A2.251 2.251 0 0 1 13.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25ZM6.75 12h.008v.008H6.75V12Zm0 3h.008v.008H6.75V15Zm0 3h.008v.008H6.75V18Z" />
                </svg>
                    <b>#</b>{{ trend.hashtag }}
              </li>
            </RouterLink>
          </div>
          <div v-if="showSuggestions" @click="toggleDisplay">
            <div
                v-for="friend in suggestions"
                v-bind:key="friend.id"
                @click="selectSuggestion(friend)"
                >
              <RouterLink :to="{name: 'profile', params: {id: friend.id}}" class="">
                <li class="pl-8 pr-2 py-1 border-b-2 border-gray-100 rounded-lg relative cursor-pointer hover:bg-yellow-50 hover:text-gray-900">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="stroke-current absolute w-4 h-4 left-2 top-2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                  </svg>
                  <b>{{ friend.name }}</b>
                </li>
              </RouterLink>
            </div>
          </div>
        </ul>
      </div>
    </div>
  </div>
    <main class="px-8 py-6 bg-blue-50">
      <RouterView />
    </main>
    <Toast />
</template>

<script>
import Toast from '@/components/Toast.vue'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export default {
  setup() {
    const userStore = useUserStore()

    return {
      userStore
    }
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
    this.userStore.initStore()

    const token = this.userStore.user.access

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

    handleInput(event) {
      // First function
      this.getUserAutoFill(event);

      // Second function
      this.getTrends();
    },

    async getUserAutoFill(event) {
      if (this.searchTerm.length === 0) {
        this.showSuggestions = false;
        return;
      }

      this.inputValue = event.target.value

      axios
        .get(`/api/search/users/${this.inputValue}/`)
        .then(response => {

            this.suggestions = response.data.matchs
            this.showSuggestions = true;
        })
        .catch(error => {
            console.log('error search:', error)
        })
    },

    async getTrends() {
      if (this.searchTerm.length === 0) {
        this.showTrends = false;
        return;
      }

      axios
        .get(`/api/posts/trends/${this.inputValue}/`)
        .then(response => {
          this.trends = response.data.trends_found
          console.log('trends', response.data.trends_found)

          // Select the top two trends
          this.trends = this.trends.slice(0, 2);
          this.showTrends = true;
        })
        .catch(error => {
          console.log('Error: ', error)
        })
    },
  
    selectTrend(trend) {
      this.searchTerm = trend.name;
      this.showTrends = false;
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
    this.getTrends()
    this.getUserAutoFill()
  },
  beforeUnmount() {
    // Remove event listener when component is unmounted
    document.body.removeEventListener('click', this.closePopUp);
  },
}
</script>


<style>
.bg-img {
  /* Set the background image */
  background-image: url('../assets/backg.jpg');
  /* Set background size, position, and repeat properties as needed */
  background-size: cover;
  /* Set the height to ensure the background image covers the container */
  height: 100vh; /* Example: full viewport height */
  width: 100vw;
  overflow: visible; /* Allows content to overflow the div */
}
</style>