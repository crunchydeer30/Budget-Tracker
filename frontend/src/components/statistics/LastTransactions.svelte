<script lang="ts">
	import { onMount } from 'svelte';
	import TableRow from '../workspace/TableRow.svelte';
	import TableCell from '../workspace/TableCell.svelte';

	import { ContainerType } from '../enums/ContainerType';
	import Container from '../workspace/Container.svelte';

	let last_transactions: any = [];

	onMount(async () => {
		await fetch('http://127.0.0.1:8000/last_transactions')
			.then((response) => response.json())
			.then((data) => {
				last_transactions = data;
			});
	});
</script>

<Container type={ContainerType.Section} classes={'col-span-4 flex flex-col gap-4 p-8'}>
	<h3 class="font-medium text-xl self-start">Последние расходы</h3>
	<section class="flex flex-col mt-4 h-full overflow-y-auto">
		<TableRow thead={true} cols={4}>
			<TableCell>Операция</TableCell>
			<TableCell>Категория</TableCell>
			<TableCell>Дата</TableCell>
			<TableCell>Стоимость</TableCell>
		</TableRow>

		{#if last_transactions.length > 0}
			{#each last_transactions as transaction}
				<TableRow cols={4}>
					<TableCell>{transaction['title']}</TableCell>
					<TableCell>{transaction['category']}</TableCell>
					<TableCell>{new Date(transaction['date']).toLocaleDateString('ru-RU')}</TableCell>
					<TableCell>{+transaction['amount']} &#8381;</TableCell>
				</TableRow>
			{/each}
		{:else}
			<p class="text-center my-12 text-xl text-gray-400">Нет данных</p>
		{/if}

		<section class="grid grid-cols-4 rounded overflow-hidden" />
	</section>
</Container>
