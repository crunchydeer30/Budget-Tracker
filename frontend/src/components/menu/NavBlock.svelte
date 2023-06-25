<script lang="ts">
	export let classes: string = '';
	
	let classNames: string[];
	classNames = classes?.split(' ') ?? [];

	$:classNames.push('w-full', 'flex', 'flex-col', 'gap-1', 'mt-20');

	$: classNames = classNames;
</script>

<nav class={classNames.join(' ')}>
	<slot />
</nav>
