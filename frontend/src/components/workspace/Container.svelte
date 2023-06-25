<script lang="ts">
	import { ContainerType } from '../enums/ContainerType';

	export let type: ContainerType;
	export let classes: string = '';

	let classNames: string[];
	classNames = classes?.split(' ') ?? [];

	$: classNames.push(
		'border',
		'border-gray-200',
		'rounded-lg',
		'bg-white',
		'shadow-sm',
		'overflow-hidden'
	);

	$: classNames = classNames;
</script>

{#if type === ContainerType.Article}
	<article class={classNames.join(' ')}>
		<slot />
	</article>
{/if}

{#if type === ContainerType.Div}
	<div class={classNames.join(' ')}>
		<slot />
	</div>
{/if}

{#if type === ContainerType.Div}
	<div class={classNames.join(' ')}>
		<slot />
	</div>
{/if}

{#if type == ContainerType.H1}
	<h1 class={classNames.join(' ')}>
		<slot />
	</h1>
{/if}

{#if type == ContainerType.H2}
	<h2 class={classNames.join(' ')}>
		<slot />
	</h2>
{/if}

{#if type == ContainerType.H3}
	<h3 class={classNames.join(' ')}>
		<slot />
	</h3>
{/if}

{#if type == ContainerType.H4}
	<h4 class={classNames.join(' ')}>
		<slot />
	</h4>
{/if}

{#if type == ContainerType.H5}
	<h5 class={classNames.join(' ')}>
		<slot />
	</h5>
{/if}

{#if type == ContainerType.H6}
	<h6 class={classNames.join(' ')}>
		<slot />
	</h6>
{/if}

{#if type == ContainerType.P}
	<p class={classNames.join(' ')}>
		<slot />
	</p>
{/if}

{#if type === ContainerType.Section}
	<section class={classNames.join(' ')}>
		<slot />
	</section>
{/if}
