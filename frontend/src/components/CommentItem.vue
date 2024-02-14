<template>
    <div class="mb-6 flex items-center justify-between">
        <div class="flex items-center space-x-6">
            <img :src="comment.owner.get_pic" class="w-[40px] rounded-full">
            
            <p>
                <strong>
                    <RouterLink :to="{name: 'profile', params:{'id': comment.owner.id}}">{{ comment.owner.name }}</RouterLink>
                </strong>
            </p>
        </div>

        <p class="text-gray-600">{{ comment.created_since }} ago</p>
    </div>

    <p>{{ comment.body }}</p> 
</template>

<script>
import { RouterLink } from 'vue-router'

export default {
    props: {
        comment: Object
    },
    components: { RouterLink }
}
</script>