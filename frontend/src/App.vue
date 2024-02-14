
<template>
      <nav class="py-6 px-8 border-b border-gray-200">
        <div class="max-w-7xl mx-auto">
            <div class="flex items-center justify-between">

                <div class="menu-left flex" v-if="userStore.user.isAuthenticated">
                  <RouterLink :to="{'name': 'feed'}" class="underline">
                    <a href="#Feed" class="text-purple-700">
                      <div class="px-6 py-3 border border-gray-500">
                        Home
                      </div>
                    </a>
                  </RouterLink>

                  <RouterLink :to="{'name': 'profile', params: {'id': userStore.user.id}}" class="underline">
                    <a href="#" class="text-purple-700">
                      <div class="px-6 py-3 border border-gray-500">
                        Collection
                      </div>                           
                    </a>
                  </RouterLink>

                </div>

                <div class="menu-right flex items-center">
                  <RouterLink :to="{'name': 'about'}" class="underline">
                    <a href="#" class="text-purple-700">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                        <path fill-rule="evenodd" d="M5.25 9a6.75 6.75 0 0 1 13.5 0v.75c0 2.123.8 4.057 2.118 5.52a.75.75 0 0 1-.297 1.206c-1.544.57-3.16.99-4.831 1.243a3.75 3.75 0 1 1-7.48 0 24.585 24.585 0 0 1-4.831-1.244.75.75 0 0 1-.298-1.205A8.217 8.217 0 0 0 5.25 9.75V9Zm4.502 8.9a2.25 2.25 0 1 0 4.496 0 25.057 25.057 0 0 1-4.496 0Z" clip-rule="evenodd" />
                      </svg>                         
                    </a>
                  </RouterLink>
                  <template v-if="userStore.user.isAuthenticated">
                      <img src="https://i.pravatar.cc/40?img=70" class="rounded-full">
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