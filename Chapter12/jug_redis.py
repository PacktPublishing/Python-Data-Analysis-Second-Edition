import jug


def main():
    jug.init('jug_demo.py', 'redis://127.0.0.1/')
    import jug_demo
    print("Merged counts", jug.task.value(jug_demo.merged_counts))

if __name__ == "__main__":
    main()
