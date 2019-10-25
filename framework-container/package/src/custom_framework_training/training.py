from __future__ import absolute_import

import logging

import sagemaker_containers.beta.framework as framework

logger = logging.getLogger(__name__)

def train(training_environment):
    logger.info('Invoking user training script.')
    
    # Execute user script as module.
    framework.modules.run_module(training_environment.module_dir, training_environment.to_cmd_args(),
                                 training_environment.to_env_vars(), training_environment.module_name)
def main():
    train(framework.training_env())