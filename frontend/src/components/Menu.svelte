<script lang="ts">
	import LogoBox from './menu/LogoBox.svelte';
	import NavBlock from './menu/NavBlock.svelte';
	import NavItem from './menu/NavItem.svelte';
</script>

<aside
	class="z-100 border-r-2 border-r-gray-200 sticky flex shrink-0 flex-col gap-8 px-4 py-6 min-h-screen w-72 overflow-hidden"
>
	<LogoBox />
	<NavBlock>
		<NavItem route="/">Статистика</NavItem>
		<NavItem route="/expenses">Расходы</NavItem>
		<NavItem route="/incomes">Доходы</NavItem>
	</NavBlock>
</aside>

<style>
</style>
