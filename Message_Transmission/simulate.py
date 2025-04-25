import matplotlib.pyplot as plt
import time

def simulates(path, sink, all_nodes, delay=1.0, color='g', share_number=None):
    fig, ax = plt.subplots()
    ax.set_title("HWSN Message Transmission Visualization")
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 120)

    # Plot all nodes
    for node_id, node in all_nodes.items():
        ax.plot(node.location[0], node.location[1], 'bo')
        ax.text(node.location[0] + 1, node.location[1] + 1, node_id, fontsize=9)

    # Plot the sink
    ax.plot(sink.location[0], sink.location[1], 'ro')
    ax.text(sink.location[0] + 1, sink.location[1] + 1, 'Sink', fontsize=9, color='red')

    # Step-by-step transmission animation
    for i in range(len(path) - 1):
        node_a = all_nodes[path[i]] if path[i] != 'sink' else sink
        node_b = all_nodes[path[i + 1]] if path[i + 1] != 'sink' else sink

        # Plot the link line with custom color
        ax.plot(
            [node_a.location[0], node_b.location[0]],
            [node_a.location[1], node_b.location[1]],
            linestyle='--',
            color=color,
            linewidth=2
        )

        # Highlight the transmitting node with custom color
        ax.plot(
            node_a.location[0],
            node_a.location[1],
            marker='o',
            markersize=10,
            color=color
        )

        # Update title with share number
        if share_number is not None:
            ax.set_title(f"Share {share_number} being transmitted", fontsize=14)

        plt.draw()
        plt.pause(delay)

    # Final link to sink if applicable
    if path[-1] == 'sink':
        second_last = all_nodes[path[-2]]
        ax.plot(
            [second_last.location[0], sink.location[0]],
            [second_last.location[1], sink.location[1]],
            linestyle='--',
            color=color,
            linewidth=2
        )

    # Highlight the sink node again
    ax.plot(sink.location[0], sink.location[1], 'ro', markersize=12)
    ax.set_title("Message fully delivered to Sink", fontsize=14)

    plt.draw()
    plt.show()
