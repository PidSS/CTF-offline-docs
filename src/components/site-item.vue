<script setup lang="ts">
    import { computed } from 'vue'

    let props = defineProps<{
        /**
         * **网站信息** \
         * 网站存储在 `public/sites` 中
         * @property name 展示的网站名称
         * @property folder *（可选）* 如果是整站填这项，网站所在文件夹名
         * @property domain *（可选）* 网站域名，是右上角复制链接的值，不填用folder替代
         * domain和folder至少填一个
         * @property indexPath *（可选）* 网站入口不是 `index.html` 的 或 单页面 填此项指向入口文件 单页面网站放在 `public/sites/散装网页` 中
         */
        site: {
            name: string,
            folder?: string,
            domain?: string,
            indexPath?: string
        }
    }>();
    const defualtSitesRoot:string = "/sites/";
    const defaultIndexPath = "/index.html";

    function open(path:string, local:boolean=true):void {
        if (local) window.open(path);
        else return;
    }

    const realDomain = computed(()=>{
        return props.site.domain? props.site.domain : props.site.folder
    })

    const realPath = computed(()=>{
        return props.site.indexPath ? props.site.indexPath : (defualtSitesRoot+props.site.folder+defaultIndexPath)
    })

    function writeClipboard(content:string|undefined):void {
        if (content)
            navigator.clipboard.writeText(content);
    }
</script>

<template>
    <div class="SiteItem" @click="open(realPath)">
        <div class="siteName">{{ site.name }}</div>
        <div class="siteDomain">{{ realDomain }}</div>
        <button class="copyBtn" @click.stop.prevent="writeClipboard(realDomain)" title="复制原网站链接到剪贴板">
            <svg t="1688046488124" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1760" id="mx_n_1688046488126" width="17" height="17"><path d="M896 768H512c-70.6 0-128-57.4-128-128V128c0-70.6 57.4-128 128-128h280.2C817.6 0 842 10.2 860 28.2L995.8 164c18 18 28.2 42.4 28.2 67.8V640c0 70.6-57.4 128-128 128zM128 256h192v96H128c-17.6 0-32 14.4-32 32v512c0 17.6 14.4 32 32 32h384c17.6 0 32-14.4 32-32v-64h96v64c0 70.6-57.4 128-128 128H128c-70.6 0-128-57.4-128-128V384c0-70.6 57.4-128 128-128z" p-id="1761" fill="#888888"></path></svg>
        </button>
        <div class="decorateRound"></div>
    </div>
</template>

<style scoped>
    @import '@/assets/main.css';

    .SiteItem {
        position: relative;
        min-width: 360px;
        min-height: 100px;
        padding: 15px 30px;
        background-color: var(--highdark);
        border-radius: 12px;
        outline: 3px solid rgba(137, 137, 137, 0.341);
        /* box-shadow: 0 0 3px 1px rgba(255, 255, 255, 0.195); */
        color: #afafaf;
        user-select: none;
        display: flex;
        flex-flow: column nowrap;
        align-items: start;
        justify-content: center;
        transition: all 0.3s;
        overflow: hidden;
    }

    .siteDomain, .siteName {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    .siteName {
        width: 100%;
        font-size: 22px;
        font-family: 元隆黑;
        z-index: 1;
        transition: inherit;
    }

    .siteDomain {
        width: 100%;
        font-size: 18px;
        font-family: Mont;
        font-weight: bold;
        opacity: 70%;
        z-index: 1;
        transition: inherit;
    }

    .SiteItem:hover {
        outline: 3px solid var(--highlight);
        box-shadow: 0 0 6px 3px var(--highlight);
    }

    .SiteItem:hover :is(.siteName, .siteDomain) {
        color: var(--vt-c-white-mute);
    }

    .copyBtn {
        position: absolute;
        z-index: 1;
        top: 10px;
        right: 10px;
        height: 28px;
        width: 28px;
        box-sizing: border-box;
        border-radius: 6px;
        border: none;
        background-color: rgb(34, 34, 34);
        outline: 2px solid rgba(101, 101, 101, 0.341);
        transition: inherit;
    }

    .copyBtn svg {
        position: relative;
        transform: translate(-50%, -50%);
        left: 50%;
        top: 40%;
        transition: inherit;
    }

    .copyBtn:hover {
        outline-color: #858585;
    }

    .copyBtn:hover svg path {
        fill: #afafaf;
    }

    .copyBtn:active {
        outline-color: #4a4a4a;
    }

    .copyBtn:active svg path {
        fill: #494949;
    }
    .decorateRound {
        position: absolute;
        height:24rem;
        width: 36rem;
        background-color: var(--litedark);
        border-radius: 50%;
        z-index: 0;
        right: 0;
        bottom: 0;
        transform: translate(55%,75%);
    }
</style>