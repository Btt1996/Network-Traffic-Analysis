import traffic_scan
import unsecured_scan
import unencrypted_scan

if __name__ == "__main__":
    # load traffic data
    data = pd.read_csv("traffic_data.csv")

    # train model
    model = traffic_scan.train_model(data)

    # scan for unsecured connections
    unsecured_scan.scan_unsecured()

    # scan for unencrypted connections
    unencrypted_scan.scan_unencrypted()
    
    # launch clustering script
    clustering_traffic.cluster_traffic(data)

    # Generate report
    with open('report.txt', 'w') as f:
        f.write("Traffic analysis report \n")
        f.write("Model accuracy: {} \n".format(accuracy))
        f.write("Number of unsecured connections found: {} \n".format(unsecured_connections))
        f.write("Number of unencrypted connections found: {} \n".format(unencrypted_connections))
        f.write("Number of clusters formed: {} \n".format(num_clusters))
    print("Report generated")
