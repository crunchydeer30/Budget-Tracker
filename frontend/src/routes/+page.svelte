<script lang="ts">
	import CategoryStats from '../components/statistics/CategoryStats.svelte';
	import LastTransactions from '../components/statistics/LastTransactions.svelte';
	import MainStats from '../components/statistics/MainStats.svelte';
	import PageHeading from '../components/workspace/PageHeading.svelte';
	import YearStats from '../components/statistics/YearStats.svelte';
	import WeekStats from '../components/statistics/WeekStats.svelte';
	import { page } from '$app/stores';
</script>

<svelte:head>
	<title>Статистика</title>
</svelte:head>

<PageHeading>Статистика</PageHeading>
<MainStats />
<section class="grid grid-cols-6 auto-rows-[500px] gap-12 mt-12">
	<YearStats />
	<WeekStats />
	<LastTransactions />
	<CategoryStats />
</section>
