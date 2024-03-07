<script>
    import projectsData from './projects.json';

    let { contact, biography, works } = projectsData;

    works = works.sort((a, b) => b.year - a.year);
</script>

<main>
	<h1>Kyle McDonald</h1>

	<div>
		<a href="https://twitter.com/{contact.twitter}" class="contact" style="float:left"
			>@{contact.twitter}</a
		>
		<a href="mailto:{contact.email}" class="contact" style="float:right">{contact.email}</a>
	</div>

	<br style="clear:both" />

	<div class="section">
		<div class="cell project">
			<h2>Biography</h2>
			<div id="bio">
				{@html biography}
			</div>
		</div>

		{#each works as work, i (work)}
			<div class="cell project">
                {#if i == 0}
                    <h2>Selected Work</h2>
                {/if}
				<a href={work.links[0].url} name={work.name} target="_blank">
					<img src={`/thumbs/${work.image}`} alt={work.name} />
				</a>
				<div class="description">
					<h3>
						{work.name}
						<em
							>{work.year}
							{#if work.client}
                                for <a href={work.client.url}>{work.client.name}</a>
							{/if}
							{#each work.collaborators as collaborator, j (collaborator)}
								{#if j === 0}
									with
								{:else}
									&nbsp;and
								{/if}
								<a href={collaborator.url}>{collaborator.name}</a>
							{/each}
						</em>
					</h3>
                    {@html work.description}
				</div>
				<ul>
					{#each work.links as link}
						<li><a href={link.url}>{link.text}</a></li>
					{/each}
				</ul>
			</div>
		{/each}
	</div>
</main>

<style>
	@import url('style.css');
</style>
