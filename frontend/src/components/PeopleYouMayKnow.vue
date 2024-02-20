<template>
<div class="p-4 bg-green-200 border border-purple-300 rounded-lg">
        <h3 class="mb-6 text-lg">Recomended artists</h3>

        <div class="border border-purple-300 rounded">
            <div class="p-2 space-y-4 overflow-y-auto max-h-52">
                <div 
                    class="flex items-center justify-between"
                    v-for="user in suggestions"
                    v-bind:key="user.id"
                >
                    <div class="flex items-center space-x-2 justify-between">
                        <img src="https://i.pravatar.cc/300?img=70" class="w-[30px] rounded-full">
                        
                        <p class="text-xs"><strong>{{ user.name }}</strong></p>

                    </div>
                    <div>
                        <RouterLink :to="{name: 'profile', params: {id: user.id}}" class="float-right py-1 px-2 bg-teal-700 text-white text-xs rounded-lg" onclick="window.location.reload()">visit</RouterLink>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'suggestions',

    data() {
        return {
            suggestions: [],
        }
    },

    mounted() {
        this.getSuggestions()
    },

    methods: {
        getSuggestions() {
            axios
                .get('/api/search/suggestions')
                .then(response => {
                    // console.log('suggus response', response.data.suggestions)

                    this.suggestions = response.data.suggestions //future algorithm to recomend users
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        }
    }
}
</script>