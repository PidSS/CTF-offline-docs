<script setup lang="ts">
import { ref, onMounted, inject } from 'vue';
import SiteItem from '@/components/site-item.vue';

let siteList = ref<{
            name: string,
            folder?: string,
            domain?: string,
            indexPath?: string
        }[]>([])
// let siteList = [
//     { name:"CTF Wiki", folder:"ctf-wiki.org" },
//     { name:"离别歌 [P神]", folder:"www.leavesongs.com" },
//     { name:"Pion1eer [机器猫]", folder:"www.ruanx.net" },
//     { name:"四川大学CTF Wiki", folder:"www.scuctf.com"},
//     { name:"Hackfun", folder:"hackfun.org" },
//     { name:"PHP5手册 (en)", folder:"php5-chunked-xhtml", domain:"php.net" },
//     { name:"PHP8手册 (zh)", folder:"php8-chunked-xhtml", domain:"php.golaravel.com" },
//     { name:"Tr0y", folder:"www.tr0y.wang" },
//     { name:"Python反序列化 [机器猫]", domain:"zhuanlan.zhihu.com/p/89132768", indexPath:"/sites/散装网页/从零开始python反序列化攻击：pickle原理解析 & 不用reduce的RCE姿势 - 知乎.html" },
//     { name:"CyberChef", folder:"CyberChef_v10.4.0" },
//     { name:"Python文档", folder:"python-3.11.4" },
//     { name:"密码学e与phi不互素的问题", domain:"tttang.com/archive/1504/#toc_2", indexPath:"sites/散装网页/针对CTFer的e与phi不互素的问题-跳跳糖.html" }
// ]
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