<script lang="ts">
	import { onMount } from 'svelte';
	import Container from '../workspace/Container.svelte';
	import { ContainerType } from '../enums/ContainerType';

	import Chart from 'chart.js/auto';

	let chartLabels: string[];
	let expenses: number[];
	let placeholder: string = '';

	let ctx: any;
	let chartCanvas: any;

	onMount(async () => {
		await loadData();
		if (expenses.length > 0) {
			await drawChart();
		} else {
			placeholder = 'Нет данных';
		}
	});

	async function loadData() {
		await fetch('http://127.0.0.1:8000/category_stats')
			.then((response) => response.json())
			.then((data) => {
				chartLabels = Object.keys(data);
				expenses = Object.values(data);
			});
	}

	async function drawChart() {
		ctx = chartCanvas.getContext('2d');
		var chart = new Chart(ctx, {
			type: 'doughnut',
			data: {
				labels: chartLabels,
				datasets: [
					{
						backgroundColor: [
							'rgb(48, 86, 211)',
							'rgb(19, 194, 150)',
							'#22A9E3',
							'#5DAD1A',
							'#843EFA'
						],
						data: expenses
					}
				]
			},
			options: {
				responsive: true,
				maintainAspectRatio: false
			}
		});
	}
</script>

<Container
	type={ContainerType.Section}
	classes={'col-span-2 flex flex-col items-center gap-8 h-full p-8'}
>
	<h3 class="font-medium text-xl self-start">Популярные категории</h3>
	<article class="w-full h-full flex flex-col items-center justify-center">
		<canvas bind:this={chartCanvas} id="myChart" class="w-0 h-0" />
		<p class="text-center text-xl text-gray-400">{placeholder}</p>
	</article>
</Container>
