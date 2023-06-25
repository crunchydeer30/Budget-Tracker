<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
	export let classes: string = '';

	let classNames: string[];
	classNames = classes?.split(' ') ?? [];

	$: classNames.push();

	$: classNames = classNames;
</script>

<div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
	<div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
	<section class="fixed inset-0 z-10 overflow-y-auto">
		<div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
			<div
				class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg"
			>
				<section class="bg-white px-4 pb-4 pt-5 sm:pt-10 sm:p-6 sm:pb-4">
					<button
						class="w-6 h-6 p-1 rounded absolute right-6 top-6 hover:bg-gray-100"
						on:click={() => {
							dispatch('closeModal');
						}}
					>
						<img src="close.svg" alt="close" />
					</button>
					<slot />
				</section>
			</div>
		</div>
	</section>
</div>
