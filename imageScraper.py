from bing_image_downloader import downloader


query_string = 'tiger' 

downloader.download(
    query_string,
    limit=70,  
    output_dir='dataset', 
    adult_filter_off=True, 
    force_replace=False,  
    timeout=60, 
    verbose=True  
)
