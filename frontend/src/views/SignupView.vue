<template>
    <div class="mx-auto grid grid-cols-2 gap-4 background-img mb-16">
        <div class="main-left">

        </div>
        <div class="main-right flex item-center">
            <div class="p-12 mt-10 mb-auto ml-40 bg-white border border-gray-200 rounded-lg bg-gray-500 bg-opacity-50">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label class="text-gray-100">Name</label><br>
                        <input type="text" v-model="form.name" placeholder="Name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label class="text-gray-100">E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="e-mail" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label class="text-gray-100">Password</label><br>
                        <input type="password" v-model="form.password1" placeholder="Password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label class="text-gray-100">Repeat password</label><br>
                        <input type="password" v-model="form.password2" placeholder="Repeat your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{  error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <div class="">
        <div class="p-12 bg-white border border-gray-200 rounded-lg">
            <h1 class="mb-6 text-2xl">Sign up</h1>

            <p class="mb-6 text-gray-500">
                Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
            </p>

            <p class="font-bold">
                Already have an account? <RouterLink :to="{ 'name': 'login' }" class="underline">Click here</RouterLink> to log in!
            </p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { useToastStore } from '@/stores/toast'


export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: '',
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
            }
            if (this.form.email === '') {
                this.errors.push('Your email is missing')
            }
            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }
            if (this.form.password2 !== this.form.password1) {
                this.errors.push('Your password does not match')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        console.log('status', response.data.status)
                        if (response.data.status === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered please log in', 'bg-emerald-500')
                            
                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            this.toastStore.showToast(5000, 'Something went wrong try again', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>

<style>
.background-img {
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