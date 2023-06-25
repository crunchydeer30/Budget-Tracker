<script lang="ts">
	import { ButtonType } from '../../components/enums/ButtonType';
	import { ContainerType } from '../../components/enums/ContainerType';
	import { onMount } from 'svelte';

	import Button from '../../components/Button.svelte';
	import ButtonDelete from '../../components/ButtonDelete.svelte';
	import Container from '../../components/workspace/Container.svelte';
	import IncomeForm from '../../components/incomes/IncomeForm.svelte';
	import PageHeading from '../../components/workspace/PageHeading.svelte';
	import TableRow from '../../components/workspace/TableRow.svelte';
	import TableCell from '../../components/workspace/TableCell.svelte';

	let transactions: any = [];
	let categories: any = [];

	let formActive = false;
	let formError = false;
	let recordCount: number;
	let nextPage: string;
	let prevPage: string;

	let searchParams: any = {
		title: '',
		page: 1,
		date: ''
	};

	$: query = Object.keys(searchParams)
		.map((k) => k + '=' + searchParams[k])
		.join('&');
	$: loadData(query);

	onMount(async () => {
		await loadData(query);
		await loadCategories();
	});

	function toggleForm() {
		formActive = !formActive;
	}

	async function loadCategories() {
		await fetch('http://127.0.0.1:8000/income_categories')
			.then((response) => response.json())
			.then((data) => {
				categories = data;
			});
	}

	async function loadData(query: any) {
		await fetch(`http://127.0.0.1:8000/incomes?${query}`)
			.then((response) => response.json())
			.then((data) => {
				prevPage = data.previous;
				nextPage = data.next;
				recordCount = data.count;
				transactions = data.results;
			});
	}

	async function addIncome(event: any) {
		const income = event.detail;
		await fetch('http://127.0.0.1:8000/incomes', {
			method: 'POST',
			body: new URLSearchParams({
				title: income.title,
				category: income.category,
				date: income.date,
				amount: income.amount
			})
		})
			.then((response) => {
				if (!response.ok) {
					formError = true;
					throw new Error(`Error: ${response.status}`);
				}
				formError = false;
				toggleForm();
				response.json();
			})
			.then((data) => {
				loadData(query);
			});
	}

	async function deleteIncome(id: string) {
		await fetch(`http://127.0.0.1:8000/incomes/${id}`, {
			method: 'DELETE'
		}).then((response) => {
			if (!response.ok) {
				throw new Error();
			}
			loadData(query);
		});
	}

	function nextPageHandler() {
		searchParams.page += 1;
	}

	function prevPageHandler() {
		searchParams.page -= 1;
	}
</script>

<svelte:head>
	<title>Доходы</title>
</svelte:head>

{#if formActive}
	<IncomeForm {formError} {categories} on:addIncome={addIncome} on:closeModal={toggleForm} />
{/if}

<PageHeading>Доходы</PageHeading>

<Button classes={'mb-6'} on:click={toggleForm}>Создать</Button>

<Container type={ContainerType.Section}>
	<section class="flex flex-col h-full overflow-y-auto">
		<TableRow thead={true} cols={5}>
			<TableCell>Операция</TableCell>
			<TableCell>Категория</TableCell>
			<TableCell>Дата</TableCell>
			<TableCell>Стоимость</TableCell>
			<TableCell>Действия</TableCell>
		</TableRow>

		{#each transactions as transaction}
			<TableRow cols={5}>
				<TableCell>{transaction['title']}</TableCell>
				<TableCell>{transaction['category']}</TableCell>
				<TableCell>{new Date(transaction['date']).toLocaleDateString('ru-RU')}</TableCell>
				<TableCell>{+transaction['amount']} &#8381;</TableCell>
				<TableCell
					><ButtonDelete
						on:click={() => {
							deleteIncome(transaction['id']);
						}}
					/></TableCell
				>
			</TableRow>
		{/each}
	</section>
</Container>

{#if recordCount > 20}
	<Container type={ContainerType.Section} classes={'w-fit p-2 mt-4 ml-auto'}>
		<div class="bg-white flex items-center gap-2">
			{#if prevPage}
				<button on:click={prevPageHandler} class="flex items-center justify-center w-1.5 h-1.5">
					<img src="arrow-left.svg" alt="prev" />
				</button>
			{/if}
			<span class="text-xl">{searchParams.page}</span>
			{#if nextPage}
				<button on:click={nextPageHandler} class="flex items-center justify-center w-1.5 h-1.5">
					<img src="arrow-right.svg" alt="prev" /></button
				>
			{/if}
		</div>
	</Container>
{/if}
