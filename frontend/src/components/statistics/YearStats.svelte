<script lang="ts">
	import { ContainerType } from '../enums/ContainerType';
	import { onMount } from 'svelte';

	import Container from '../workspace/Container.svelte';
	import Chart from 'chart.js/auto';

	let incomes: number[];
	let expenses: number[];
	let ctx: any;
	let chartCanvas: any;

	let chartLabels = [
		'Январь',
		'Февраль',
		'Март',
		'Апрель',
		'Май',
		'Июнь',
		'Июль',
		'Август',
		'Сентябрь',
		'Октябрь',
		'Ноябрь',
		'Декабрь'
	];

	onMount(async () => {
		await loadData();
		await drawChart();
	});

	async function loadData() {
		await fetch('http://127.0.0.1:8000/year_stats')
			.then((response) => response.json())
			.then((data) => {
				incomes = data['incomes'];
				expenses = data['expenses'];
			});
	}

	async function drawChart() {
		ctx = chartCanvas.getContext('2d');
		var chart = new Chart(ctx, {
			type: 'line',
			data: {
				labels: chartLabels,
				datasets: [
					{
						label: 'Доходы',
						backgroundColor: 'rgb(19, 194, 150)',
						borderColor: 'rgb(19, 194, 150)',
						data: incomes
					},
					{
						label: 'Расходы',
						backgroundColor: 'rgb(48, 86, 211)',
						borderColor: 'rgb(48, 86, 211)',
						data: expenses
					}
				]
			},
			options: {
				responsive: true,
				maintainAspectRatio: false,
				elements: {
					line: {
						tension: 0.4
					}
				},
				scales: {
					x: {
						grid: {
							display: false
						}
					},

					y: {
						grid: {
							display: false
						}
					}
				}
			}
		});
	}
</script>

<Container
	type={ContainerType.Section}
	classes={'col-span-4 flex h-full gap-10 items-center flex-col justify-center p-8'}
>
	<h3 class="font-medium text-xl self-start">Статистика за год</h3>
	<article class="w-full h-full">
		<canvas bind:this={chartCanvas} id="myChart" />
	</article>
</Container>
