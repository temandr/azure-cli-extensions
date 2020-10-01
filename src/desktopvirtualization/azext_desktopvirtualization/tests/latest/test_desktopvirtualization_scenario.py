# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from .. import try_manual, raise_if
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    pass


# EXAMPLE: /HostPools/put/HostPool_Create
@try_manual
def step__hostpools_put_hostpool_create(test, rg):
    test.cmd('az desktopvirtualization hostpool create '
             '--location "centralus" '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--host-pool-type "Pooled" '
             '--load-balancer-type "BreadthFirst" '
             '--max-session-limit 999999 '
             '--personal-desktop-assignment-type "Automatic" '
             '--registration-info expiration-time="2020-08-20T08:57:45.479Z" registration-token-operation="Update" '
             '--sso-context "KeyVaultPath" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myHostPool}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /HostPools/get/HostPool_Get
@try_manual
def step__hostpools_get_hostpool_get(test, rg):
    test.cmd('az desktopvirtualization hostpool show '
             '--name "{myHostPool}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /HostPools/get/HostPool_List
@try_manual
def step__hostpools_get_hostpool_list(test, rg):
    test.cmd('az desktopvirtualization hostpool list '
             '-g ""',
             checks=[])


# EXAMPLE: /HostPools/get/HostPool_ListByResourceGroup
@try_manual
def step__hostpools_get_hostpool_listbyresourcegroup(test, rg):
    test.cmd('az desktopvirtualization hostpool list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /HostPools/patch/HostPool_Update
@try_manual
def step__hostpools_patch_hostpool_update(test, rg):
    test.cmd('az desktopvirtualization hostpool update '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--load-balancer-type "BreadthFirst" '
             '--max-session-limit 999999 '
             '--personal-desktop-assignment-type "Automatic" '
             '--registration-info expiration-time="2020-08-20T08:57:45.522Z" registration-token-operation="Update" '
             '--sso-context "KeyVaultPath" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myHostPool}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /ApplicationGroups/put/ApplicationGroup_Create
@try_manual
def step__applicationgroups_put_applicationgroup_create(test, rg):
    test.cmd('az desktopvirtualization applicationgroup create '
             '--location "centralus" '
             '--description "des1" '
             '--application-group-type "RemoteApp" '
             '--friendly-name "friendly" '
             '--host-pool-arm-path "/subscriptions/{subscription_id}/resourcegroups/{rg}/providers/Microsoft.DesktopVir'
             'tualization/hostpools/{myHostPool}" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myApplicationGroup}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /ApplicationGroups/get/ApplicationGroup_Get
@try_manual
def step__applicationgroups_get_applicationgroup_get(test, rg):
    test.cmd('az desktopvirtualization applicationgroup show '
             '--name "{myApplicationGroup}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /ApplicationGroups/get/ApplicationGroup_List
@try_manual
def step__applicationgroups_get_applicationgroup_list(test, rg):
    test.cmd('az desktopvirtualization applicationgroup list '
             '--filter "applicationGroupType eq \'RailApplication\'" '
             '-g ""',
             checks=[])


# EXAMPLE: /ApplicationGroups/get/ApplicationGroup_ListByResourceGroup
@try_manual
def step__applicationgroups_get_applicationgroup_listbyresourcegroup(test, rg):
    test.cmd('az desktopvirtualization applicationgroup list '
             '--filter "applicationGroupType eq \'RailApplication\'" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /ApplicationGroups/patch/ApplicationGroups_Update
@try_manual
def step__applicationgroups_patch_applicationgroups_update(test, rg):
    test.cmd('az desktopvirtualization applicationgroup update '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myApplicationGroup}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /ApplicationGroups/delete/ApplicationGroup_Delete
@try_manual
def step__applicationgroups_delete_applicationgroup_delete(test, rg):
    test.cmd('az desktopvirtualization applicationgroup delete '
             '--name "{myApplicationGroup}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Workspaces/put/Workspace_Create
@try_manual
def step__workspaces_put_workspace_create(test, rg):
    test.cmd('az desktopvirtualization workspace create '
             '--resource-group "{rg}" '
             '--location "centralus" '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /Workspaces/get/Workspace_Get
@try_manual
def step__workspaces_get_workspace_get(test, rg):
    test.cmd('az desktopvirtualization workspace show '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /Workspaces/get/Workspace_ListByResourceGroup
@try_manual
def step__workspaces_get_workspace_listbyresourcegroup(test, rg):
    test.cmd('az desktopvirtualization workspace list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Workspaces/get/Workspace_ListBySubscription
@try_manual
def step__workspaces_get_workspace_listbysubscription(test, rg):
    test.cmd('az desktopvirtualization workspace list '
             '-g ""',
             checks=[])


# EXAMPLE: /Workspaces/patch/Workspace_Update
@try_manual
def step__workspaces_patch_workspace_update(test, rg):
    test.cmd('az desktopvirtualization workspace update '
             '--resource-group "{rg}" '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /HostPools/delete/HostPool_Delete
@try_manual
def step__hostpools_delete_hostpool_delete(test, rg):
    test.cmd('az desktopvirtualization hostpool delete '
             '--force true '
             '--name "{myHostPool}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Workspaces/delete/Workspace_Delete
@try_manual
def step__workspaces_delete_workspace_delete(test, rg):
    test.cmd('az desktopvirtualization workspace delete '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=[])


@try_manual
def cleanup(test, rg):
    pass


@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step__hostpools_put_hostpool_create(test, rg)
    step__hostpools_get_hostpool_get(test, rg)
    step__hostpools_get_hostpool_list(test, rg)
    step__hostpools_get_hostpool_listbyresourcegroup(test, rg)
    step__hostpools_patch_hostpool_update(test, rg)
    step__applicationgroups_put_applicationgroup_create(test, rg)
    step__applicationgroups_get_applicationgroup_get(test, rg)
    step__applicationgroups_get_applicationgroup_list(test, rg)
    step__applicationgroups_get_applicationgroup_listbyresourcegroup(test, rg)
    step__applicationgroups_patch_applicationgroups_update(test, rg)
    step__applicationgroups_delete_applicationgroup_delete(test, rg)
    step__workspaces_put_workspace_create(test, rg)
    step__workspaces_get_workspace_get(test, rg)
    step__workspaces_get_workspace_listbyresourcegroup(test, rg)
    step__workspaces_get_workspace_listbysubscription(test, rg)
    step__workspaces_patch_workspace_update(test, rg)
    step__hostpools_delete_hostpool_delete(test, rg)
    step__workspaces_delete_workspace_delete(test, rg)
    cleanup(test, rg)


@try_manual
class DesktopVirtualizationAPIClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestdesktopvirtualization_resourceGroup1'[:7], key='rg',
                           parameter_name='rg')
    def test_desktopvirtualization(self, rg):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myWorkspace': 'workspace1',
            'myHostPool': 'hostPool1',
            'myApplicationGroup': 'applicationGroup1',
        })

        call_scenario(self, rg)
        raise_if()
