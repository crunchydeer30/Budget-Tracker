<script lang="ts">
	import { onMount } from 'svelte';
	import StatCard from './StatCard.svelte';
	import { StatType } from '../enums/StatType';

	let year_incomes = '';
	let year_expenses = '';
	let month_incomes = '';
	let month_expenses = '';

	onMount(async () => {
		await loadData();
	});

	async function loadData() {
		await fetch('http://127.0.0.1:8000/main_stats')
			.then((response) => response.json())
			.then((data) => {
				year_incomes = data.incomes.year;
				year_expenses = data.expenses.year;
				month_incomes = data.incomes.month;
				month_expenses = data.expenses.month;
			});
	}
</script>

<section class="grid grid-cols-4 gap-6">
	<StatCard data={month_incomes} type={StatType.Income}>
		<p slot="timeframe">Доходы за месяц</p>
		<p slot="increase_timeframe">Прошлый месяц</p>
	</StatCard>
	<StatCard data={month_expenses} type={StatType.Expense}>
		<p slot="timeframe">Расходы за месяц</p>
		<p slot="increase_timeframe">Прошлый месяц</p>
	</StatCard>
	<StatCard data={year_incomes} type={StatType.Income}>
		<p slot="timeframe">Доходы за год</p>
		<p slot="increase_timeframe">Прошлый год</p>
	</StatCard>
	<StatCard data={year_expenses} type={StatType.Expense}>
		<p slot="timeframe">Расходы за год</p>
		<p slot="increase_timeframe">Прошлый год</p>
	</StatCard>
</section>
