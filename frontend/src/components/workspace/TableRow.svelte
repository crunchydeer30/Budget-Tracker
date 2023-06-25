<script lang="ts">
	export let thead: boolean = false;
	export let cols: number;
</script>

<section
	style={`grid-template-columns: repeat(${cols}, 1fr)`}
	class="grid overflow-hidden shrink-0 border-b border-b-gray hover:bg-gray-50 duration-200"
	class:font-bold={thead}
>
	<slot />
</section>
