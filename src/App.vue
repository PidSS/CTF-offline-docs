<script setup lang="ts">
import { ref, onMounted, inject } from 'vue';
import SiteItem from '@/components/site-item.vue';

let siteList = ref<{
            name: string,
            folder?: string,
            domain?: string,
            indexPath?: string
        }[]>([])

const axios: any = inject('axios')  // inject axios
onMounted(()=>{
    axios
        .get("/json/properties.json")
        .then((res:{data:any})=>{
            siteList.value = res.data.sites;
    })
})

</script>

<template>
    <div id="title">「 离线文档 」</div>
    <div id="content">
        <SiteItem v-for="item of siteList" :site="item"></SiteItem>
    </div>
</template>

<style scoped>
    @import './assets/main.css';

    #title {
        text-align: center;
        font-size: 64px;
        line-height: 120px;
        height: 120px;
        margin: 40px auto;
        color: var(--vt-c-white-mute);
        font-family: 元隆黑;
    }

    #content {
        width: 80vw;
        height: 80vh;
        margin: auto;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
        grid-template-rows: repeat(auto-fit, 120px);
        row-gap: 20px;
        column-gap: 20px;
    }
</style>