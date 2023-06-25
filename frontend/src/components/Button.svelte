<script lang="ts">
	import { ButtonType } from './enums/ButtonType';
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

	export let classes: string = '';
	export let type: ButtonType = ButtonType.Button;

	let classNames: string[];
	classNames = classes?.split(' ') ?? [];

	$: classNames.push(
		'text-lg',
		'bg-primary',
		'text-white',
		'rounded-lg',
		'py-2',
		'px-4',
		'hover:bg-primary-dark',
		'duration-200'
	);

	$: classNames = classNames;
</script>

<button class={classNames.join(' ')} {type} on:click>
	<slot />
</button>
