<script lang="ts">
	import Modal from '../workspace/Modal.svelte';
	import Button from '../Button.svelte';
	import { ButtonType } from '../enums/ButtonType';
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

	let title: string = '';
	let category: string = '';
	let date: string = '';
	let amount = '';

	export let categories: any = [];
	export let formError: boolean;
</script>

<Modal on:closeModal>
	<form
		class="flex flex-col gap-5"
		on:submit|preventDefault={() =>
			dispatch('addExpense', {
				title: title,
				category: category,
				date: date,
				amount: amount
			})}
	>
		<h3 class="font-semibold text-2xl">Новый расход</h3>
		<div class="space-y-2">
			<label for="title">Название</label>
			<input
				bind:value={title}
				type="text"
				class="border w-full px-3 py-1 rounded"
				id="title"
				placeholder="Название"
				maxlength="25"
				required
			/>
		</div>

		<div class="space-y-2">
			<label for="category">Категория</label>
			<select
				bind:value={category}
				name="category"
				id="category"
				class="border w-full px-2 py-1 rounded"
				required
			>
				<option value="">---</option>
				{#each categories as category}
					<option value={category.id}>{category.title}</option>
				{/each}
			</select>
		</div>

		<div class="space-y-2">
			<label for="date">Дата</label>
			<input
				bind:value={date}
				type="date"
				class="border w-full px-3 py-1 rounded"
				id="date"
				placeholder="Дата"
				required
			/>
		</div>

		<div class="space-y-2">
			<label for="amount">Стоимость</label>
			<input
				bind:value={amount}
				type="number"
				class="border w-full px-3 py-1 rounded"
				id="amount"
				placeholder="Стоимость"
				required
				min="0"
			/>
		</div>
		{#if formError}
			<p class="text-red-600 text-lg text-center">Неверные данные!</p>
		{/if}
		<Button classes={'mt-4'} type={ButtonType.Submit}>Сохранить</Button>
	</form>
</Modal>
