<script lang="ts">
	import Container from '../workspace/Container.svelte';
	import { ContainerType } from '../enums/ContainerType';

	import Chart from 'chart.js/auto';
	let chartData;
	import { onMount } from 'svelte';

	let chartLabels = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'];
	let expenses: number[];
	let incomes: number[];

	let ctx;
	let chartCanvas: any;

	onMount(async () => {
		await loadData();
		await drawChart();
	});

	async function drawChart() {
		ctx = chartCanvas.getContext('2d');
		var chart = new Chart(ctx, {
			type: 'bar',
			data: {
				labels: chartLabels,
				datasets: [
					{
						label: 'Доходы',
						backgroundColor: '#13c296',
						borderColor: '#13c296',
						borderRadius: 12,
						data: incomes,
						stack: '1'
					},
					{
						label: 'Расходы',
						backgroundColor: '#3056d3',
						borderColor: '#3056d3',
						borderRadius: 12,
						data: expenses,
						stack: '2'
					}
				]
			},
			options: {
				responsive: true,
				maintainAspectRatio: false,
				barThickness: 10,
				interaction: {
					intersect: false
				},
				scales: {
					x: {
						stacked: true,
						grid: {
							display: false
						}
					},

					y: {
						stacked: true,
						grid: {
							display: true
						}
					}
				}
			}
		});
	}

	async function loadData() {
		await fetch('http://127.0.0.1:8000/week_stats')
			.then((response) => response.json())
			.then((data) => {
				incomes = data['incomes'];
				expenses = data['expenses'];
			});
	}
</script>

<Container
	type={ContainerType.Section}
	classes={'col-span-2 flex flex-col items-center gap-10 h-full p-8'}
>
	<h3 class="font-medium text-xl self-start">Статистика за неделю</h3>
	<article class="h-full w-full">
		<canvas bind:this={chartCanvas} id="myChart" />
	</article>
</Container>
