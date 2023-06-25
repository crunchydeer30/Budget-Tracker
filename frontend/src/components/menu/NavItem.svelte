<script lang="ts">
	import { page } from '$app/stores';

	export let route: string;
	export let classes: string = '';
	export let active: boolean = false;

	$: if ($page.url.pathname === route) {
		active = true;
	} else {
		active = false;
	}

	let classNames: string[];
	classNames = classes?.split(' ') ?? [];

	$: classNames.push(
		'flex',
		'items-center',
		'gap-2',
		'group',
		'rounded-lg',
		'px-4',
		'py-2',
		'hover:bg-primary',
		'hover:text-white',
		'text',
		'text-lg',
		'font-medium',
		'text-font-secondary',
		'duration-200'
	);

	$: classNames = classNames;
</script>

<a href={route} class={classNames.join(' ')} class:bg-primary={active} class:text-white={active}>
	<slot />
</a>
