function getCommitsDetails(commitData) {
    if(commitData.commit) {
        return {
            message: commitData.commit.message.split("\n")[0],
            date: commitData.commit.author.date
        };
    }
    return {
        message: commitData.message,
        date: commitData.date
    };
}

export function renderRepoInfo(repo) {
    const container = document.getElementById("repo-stats");
    if(!container) return;

    container.innerHTML = "";

    const heading = document.createElement("h2");
    heading.textContent = repo.name;

    const desc = document.createElement("p");
    desc.textContent = repo.description || "No description";

    const stats = document.createElement("span");
    stats.textContent = `⭐ ${repo.stargazers_count}`;

    container.append(heading, desc, stats);
}

export function renderCommits(commits) {
    const container = document.getElementById("commits-list");
    if (!container) return;
    
    container.innerHTML = "";
    
    commits.forEach(commitData => {
        const div = document.createElement("div");
        div.className = "commit-item";
        
        const details = getCommitsDetails(commitData);
        const date = new Date(details.date).toLocaleDateString();
        
        div.textContent = `${date}: ${details.message}`;
        container.appendChild(div);
    });
}

export function matchTaskToCommit(task, commits) {
    const match = commits.find(commitData => { 
        const details = getCommitsDetails(commitData);
        return details.message.toLowerCase().includes(task.title.toLowerCase()) 
    });
    return match || null;
}

export function mergeTasks(tasks, commits) {
    return tasks.map(task => ({
        task: task,
        matchedCommit: matchTaskToCommit(task, commits)
    }));    
}

export function renderTasks(tasks, commits) {
    const container = document.getElementById("tasks-list");
    if (!container) return;
    
    container.innerHTML = "";
    
    const mergedData = mergeTasks(tasks, commits);
    
    mergedData.forEach(item => {
        const taskDiv = document.createElement("div");
        taskDiv.className = `task-item status-${item.task.status.toLowerCase()}`;
        taskDiv.textContent = `[${item.task.status}] ${item.task.title}`;
        
        const ul = document.createElement("ul");
        const li = document.createElement("li");
        
        if (item.matchedCommit) {
            const details = getCommitsDetails(item.matchedCommit);
            const date = new Date(details.date).toLocaleString();
            li.textContent = `${date} - ${details.message}`;
        } else {
            li.textContent = "no matching activity yet.";
            li.style.color = "#757575";
            li.style.fontStyle = "italic";
        }
        
        ul.appendChild(li);
        taskDiv.appendChild(ul);
        container.appendChild(taskDiv);
    });
}