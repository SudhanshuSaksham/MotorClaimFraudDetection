import os
import shutil

from Utils import Utils_Configurations

config_file_path = os.path.join(os.getcwd(), "config.ini")
config_file = Utils_Configurations.Configuration(config_file_path)


def create_folder(folder_path, delete_existing=False, testing=False):
    if os.path.exists(folder_path):
        if delete_existing and not testing:
            shutil.rmtree(folder_path)
            os.makedirs(folder_path)
    else:
        os.makedirs(folder_path)


# Get the root path of the project
def get_root_path():
    path = config_file.read_configuration_options("ROOT PATH", "root_path", "str")
    return path


def get_data_file():
    data_file = config_file.read_configuration_options("DATASET", "data_file", "str")
    return data_file


# Get the folder names of the project
def get_folder_names():
    data_folder = config_file.read_configuration_options("FOLDERS", "dataset_folder", "str")
    raw = config_file.read_configuration_options("FOLDERS", "raw_dataset_folder", "str")
    preprocessed = config_file.read_configuration_options("FOLDERS", "preprocessed_dataset", "str")
    final = config_file.read_configuration_options("FOLDERS", "final_dataset_folder", "str")
    model = config_file.read_configuration_options("FOLDERS", "final_model_folder", "str")
    model_viz = config_file.read_configuration_options("FOLDERS", "result_visualisation_folder", "str")
    model_res = config_file.read_configuration_options("FOLDERS", "model_results_folder", "str")
    model_resources = config_file.read_configuration_options("FOLDERS", "model_resources_folder", "str")
    model_combined = config_file.read_configuration_options("FOLDERS", "model_combined_results_folder", "str")
    return data_folder, raw, preprocessed, final, model, model_viz, model_res, model_resources, model_combined


def get_train_test_split_params():
    ratio = config_file.read_configuration_options("TRAIN TEST SPLIT", "split_ratio", "float")
    return ratio


def get_model_params():
    shuffle = config_file.read_configuration_options("MODEL PARAMETERS", "shuffle", "bool")
    random_state = config_file.read_configuration_options("MODEL PARAMETERS", "random_state", "int")
    no_of_splits = config_file.read_configuration_options("MODEL PARAMETERS", "n_splits", "int")
    no_of_iters = config_file.read_configuration_options("MODEL PARAMETERS", "n_iter", "int")
    return shuffle, random_state, no_of_splits, no_of_iters


def get_dataframe_preprocessing_flags():
    duplicate = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS", "drop_duplicate_records", "bool")
    one_hot_encoding_cols = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS",
                                                                   "one_hot_encoding_columns", "list")
    label_encoding_cols = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS",
                                                                 "label_encoding_target_column", "list")
    count_frequency_encoding_cols = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS",
                                                                           "count_frequency_encoding_columns", "list")
    ordinal_encoding_cols = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS",
                                                                   "ordinal_encoding_columns", "list")
    drop_cols = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS", "columns_to_be_dropped", "list")
    date_cols = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS", "date_based_columns", "list")
    cat_cols = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS", "category_based_columns", "list")
    int_cols = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS", "integer_based_columns", "list")
    float_cols = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS", "float_based_columns", "list")
    target_col = config_file.read_configuration_options("COLUMN PREPROCESSING FLAGS", "target_column", "str")
    return duplicate, one_hot_encoding_cols, label_encoding_cols, count_frequency_encoding_cols, ordinal_encoding_cols, drop_cols, date_cols, cat_cols, int_cols, float_cols, target_col


def get_class_imbalance_params():
    imbalance_flag = config_file.read_configuration_options("CLASS IMBALANCE", "class_imbalance_flag", "bool")
    imbalance_method = config_file.read_configuration_options("CLASS IMBALANCE", "class_imbalance_method", "str")
    return imbalance_flag, imbalance_method


def get_normalization_params():
    scaling_flag = config_file.read_configuration_options("NORMALISATION", "scaling", "bool")
    scaling_method = config_file.read_configuration_options("NORMALISATION", "scaling_method", "str")
    return scaling_flag, scaling_method


def get_hyperparameter_tuning_methods():
    hyperparamater_flag = config_file.read_configuration_options("HYPERPARAMETER TUNING METHODS",
                                                                 "hyperparamater_tuning", "bool")
    hyperparamater_method = config_file.read_configuration_options("HYPERPARAMETER TUNING METHODS",
                                                                   "hyperparameter_method", "str")
    return hyperparamater_flag, hyperparamater_method


def get_decision_tree_classifier_hyperparameter():
    decision_params = config_file.read_configuration_options("DECISION TREE CLASSIFIER PARAMETERS",
                                                             "decision_tree_params", "dict")
    return decision_params


def get_random_forest_classifier_hyperparameter():
    random_forest_params = config_file.read_configuration_options("RANDOM FOREST CLASSIFIER PARAMETERS",
                                                                  "random_forest_params", "dict")
    return random_forest_params


def get_xgboost_classifier_hyperparameter():
    xgb_params = config_file.read_configuration_options("XGBOOST CLASSIFIER PARAMETERS", "xgboost_params", "dict")
    return xgb_params


def get_algo_list_for_model_training():
    algo_list = config_file.read_configuration_options("MODELS TRAINING", "models_list", "list")
    return algo_list


def get_model_prediction_threshold():
    thresh = config_file.read_configuration_options("MODEL PREDICTION", "threshold", "float")
    return thresh


def get_causality_parameter_values():
    pred_thresh = config_file.read_configuration_options("CAUSALITY", "prediction_threshold", "float")
    no_of_causalities = config_file.read_configuration_options("CAUSALITY", "number_of_causalities", "int")
    number_of_Decimals = config_file.read_configuration_options("CAUSALITY", "fraudScore_Number_of_Decimals", "int")
    return pred_thresh, no_of_causalities, number_of_Decimals


def get_server_details():
    port_number = config_file.read_configuration_options("SERVER", "port", "int")
    return port_number


root_path = get_root_path()
data_file = get_data_file()
dataset_folder, raw_dataset_folder, preprocessed_dataset_folder, final_dataset_folder, best_model_folder, \
model_visualization_folder, model_results_folder, model_resources_folder, model_combined_results_folder = get_folder_names()

dataset_file = os.path.join(dataset_folder, raw_dataset_folder, data_file)

dataset_path = os.path.join(root_path, dataset_folder)
preprocessed_dataset_path = os.path.join(dataset_path, preprocessed_dataset_folder)
final_dataset_path = os.path.join(dataset_path, final_dataset_folder)
model_visualization_path = os.path.join(root_path, model_visualization_folder)
model_resources_path = os.path.join(root_path, model_resources_folder)
best_model_path = os.path.join(root_path, best_model_folder)
model_results_path = os.path.join(root_path, model_results_folder)
model_combined_results_path = os.path.join(root_path, model_combined_results_folder)

train_test_ratio_split = get_train_test_split_params()

class_imbalance_flag, class_imbalance_method = get_class_imbalance_params()

shuffle_flag, random_state_number, n_splits, n_iters = get_model_params()

drop_duplicate_records, one_hot_encoding_columns, label_encoding_columns, count_frequency_encoding_columns, ordinal_encoding_columns, drop_columns, date_columns, cat_columns, int_columns, float_columns, target_column = get_dataframe_preprocessing_flags()

normalisation_flag, normalisation_method = get_normalization_params()

hyperparameter_tuning_flag, hyperparameter_tuning_method = get_hyperparameter_tuning_methods()

decision_tree_hyperparameter = get_decision_tree_classifier_hyperparameter()

randomforest_hyperparameter = get_random_forest_classifier_hyperparameter()

xgboost_hyperparameter = get_xgboost_classifier_hyperparameter()

algorithm_list = get_algo_list_for_model_training()

threshold = get_model_prediction_threshold()

prediction_threshold, number_of_causalities, fraudScore_Number_of_Decimals = get_causality_parameter_values()

port = get_server_details()


def create_folders():
    create_folder(preprocessed_dataset_path, delete_existing=False, testing=True)
    create_folder(final_dataset_path, delete_existing=False, testing=True)
    create_folder(model_visualization_path, delete_existing=False, testing=True)
    create_folder(model_resources_path, delete_existing=False, testing=True)
    create_folder(best_model_path, delete_existing=False, testing=True)
    create_folder(model_results_path, delete_existing=False, testing=True)
    create_folder(model_combined_results_path, delete_existing=False, testing=True)


create_folders()

if __name__ == '__main__':
    pass
