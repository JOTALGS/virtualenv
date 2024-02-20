<template>
    <div class="p-4 bg-teal-100 border border-purple-300 rounded-lg max">
        <h3 class="mb-6 text-xl">Trends</h3>
        <div class="border border-purple-300 rounded">
            <div class="p-2 space-y-4 overflow-y-auto max-h-32">
                <div 
                    class="flex items-center justify-between"
                    v-for="trend in trends"
                    v-bind:key="trend.id"
                >
                    <p class="text-xs">
                        <strong>#{{ trend.hashtag }}</strong><br>
                        <span class="text-gray-500" >{{ trend.occurences }} posts</span>
                    </p>

                    <RouterLink :to="{name: 'trendview', params: {id: trend.hashtag}}" class="py-1 px-2 bg-teal-700 text-white text-xs rounded-lg" onclick="window.location.reload()">Explore</RouterLink>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'trends',

    data() {
        return {
            trends: [],
        }
    },

    mounted() {
        this.getTrends()
    },

    methods: {
        getTrends() {
            axios
                .get('/api/posts/top/trends/')
                .then(response => {
                    //console.log('trend response', response.data)

                    this.trends = response.data.slice(0, 5) //future add logic to retrieve higer occurences
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        }
    }
}
</script>