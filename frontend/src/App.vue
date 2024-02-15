
<template>
      <nav class="py-6 px-8 border-b border-gray-200">
        <div class="max-w-7xl mx-auto">
            <div class="flex items-center justify-between">
                <div class="menu-left">
                    <a href="#" class="font-mono text-4xl">TRIBU</a>
                </div>
                <div>
                    <input type="text" v-model="searchQuery" class="border border-gray-300 px-3 py-1 rounded-md">
                    <button @click="search" class="text-black-100 text-black px-4 py-1 rounded-md ml-2">Search</button>
                </div>

                <div class="menu-center flex" v-if="userStore.user.isAuthenticated">
                </div>

                <div class="menu-right flex items-center space-x-4">
                  <RouterLink :to="{'name': 'feed'}" class="">
                    <a href="#Feed" class="text-black-100">
                      <div class="px-6 py-3 border border-gray-500 rounded bg-neutral-200 hover:bg-blue-300 flex items-center space-x-2">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
                          <path d="M23 9v2h-2v7a3 3 0 01-3 3h-4v-6h-4v6H6a3 3 0 01-3-3v-7H1V9l11-7 5 3.18V2h3v5.09z"></path>
                        </svg>
                        <span>Home</span>
                      </div>
                    </a>
                  </RouterLink>

                  <RouterLink :to="{'name': 'profile', params: {'id': userStore.user.id}}" class="">
                    <a href="#" class="text-black-100">
                      <div class="px-6 py-3 border border-gray-500 rounded bg-neutral-200 hover:bg-blue-300 flex items-center space-x-2">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 9.776c.112-.017.227-.026.344-.026h15.812c.117 0 .232.009.344.026m-16.5 0a2.25 2.25 0 0 0-1.883 2.542l.857 6a2.25 2.25 0 0 0 2.227 1.932H19.05a2.25 2.25 0 0 0 2.227-1.932l.857-6a2.25 2.25 0 0 0-1.883-2.542m-16.5 0V6A2.25 2.25 0 0 1 6 3.75h3.879a1.5 1.5 0 0 1 1.06.44l2.122 2.12a1.5 1.5 0 0 0 1.06.44H18A2.25 2.25 0 0 1 20.25 9v.776" />
                        </svg>
                        <span>Collection</span>
                      </div>
                    </a>
                  </RouterLink>

                  <RouterLink :to="{'name': 'about'}" class="">
                    <a href="#" class="text-black-100">
                      <div class="px-6 py-3 border border-gray-500 rounded bg-neutral-200 hover:bg-blue-300 flex items-center space-x-2">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                          <path fill-rule="evenodd" d="M5.25 9a6.75 6.75 0 0 1 13.5 0v.75c0 2.123.8 4.057 2.118 5.52a.75.75 0 0 1-.297 1.206c-1.544.57-3.16.99-4.831 1.243a3.75 3.75 0 1 1-7.48 0 24.585 24.585 0 0 1-4.831-1.244.75.75 0 0 1-.298-1.205A8.217 8.217 0 0 0 5.25 9.75V9Zm4.502 8.9a2.25 2.25 0 1 0 4.496 0 25.057 25.057 0 0 1-4.496 0Z" clip-rule="evenodd" />
                        </svg>
                        <span>News</span>
                      </div>             
                    </a>
                  </RouterLink>

                  <template v-if="userStore.user.isAuthenticated">
                      <div class="flex items-center space-x-2 border border-gray-500 rounded px-3 py-1 bg-neutral-200">
                      <img src="https://i.pravatar.cc/40?img=70" class="rounded-full">
                      <span>Profile</span>
                      </div>
                  </template>
                  <template v-else>
                    <RouterLink to="/login" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Log in</RouterLink>
                    <RouterLink to="/signup" class="py-4 px-6 bg-blue-600 text-white rounded-lg">Sign up</RouterLink>
                  </template>
                </div>
            </div>
        </div>
    </nav>
    <main class="px-8 py-6 bg-gray-100">
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
  }
}
</script>