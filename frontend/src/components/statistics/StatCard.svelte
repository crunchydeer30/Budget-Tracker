<script lang="ts">
	import { ContainerType } from '../enums/ContainerType';
	import Container from '../workspace/Container.svelte';

	import { StatType } from '../enums/StatType';
	import ExpenseForm from '../expenses/ExpenseForm.svelte';

	export let data: any;
	export let type: StatType;
</script>

<Container type={ContainerType.Article} classes={'py-4 px-6 flex flex-col justify-between'}>
	{#if data}
		<div class="text-font-secondary mb-6">
			<slot name="timeframe" />
		</div>
		<p class="font-semibold text-2xl mb-3">
			{data.value} &#8381;
		</p>
		<div class="flex justify-between items-center text-font-secondary gap-3">
			{#if data.increase >= 0}
				<p
					class:text-green-600={type == StatType.Income}
					class:text-red-600={type == StatType.Expense}
				>
					+{data.increase.toFixed(1)}%
				</p>
			{:else}
				<p
					class:text-red-600={type == StatType.Income}
					class:text-green-600={type == StatType.Expense}
				>
					{data.increase.toFixed(1)}%
				</p>
			{/if}
			<div class="text-sm">
				<slot name="increase_timeframe" />
			</div>
		</div>
	{/if}
</Container>
